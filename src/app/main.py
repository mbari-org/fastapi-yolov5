# !/usr/bin/env python
__author__ = "Danelle Cline"
__copyright__ = "Copyright 2023, MBARI"
__credits__ = ["MBARI"]
__license__ = "GPL"
__maintainer__ = "Danelle Cline"
__email__ = "dcline at mbari.org"
__doc__ = '''

Runs a FastAPI server to serve a YOLOv5 model

@author: __author__
@status: __status__
@license: __license__
'''

import numpy as np
import io
from fastapi import FastAPI, File, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import Response
from app.load import load_yolov5, scale_image
from app import __version__
from PIL import Image

model, description = load_yolov5()

app = FastAPI(
    title=description,
    description=f"""Runs inference on underwater images. 
                    Predicts (bounding box) localizations in images using the YOLOV5 {description}.
                    Upload an image and the API returns the results in JSON format or an image.""",
    version=__version__
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BoundingBox(BaseModel):
    class_id: int
    class_name: str
    width: float
    height: float
    x: float
    y: float
    confidence: float


@app.get('/health')
def get_health():
    """
    Health check endpoint. Returns 200 and an OK message if the API is up and running and the model is loaded.
    """
    try:
        # Check if model is loaded simply by checking if the model has a names attribute
        model.names
    except Exception as e:
        return Response(status_code=500, content=str(e))

    return {"message": "OK"}


@app.post("/predict")
def upload(file: UploadFile = File(...), confidence_threshold: float = 0.01) -> list[BoundingBox]:
    """
    Upload an image file and return the predictions in JSON format.

    To use, send a POST request with the **files** parameter as the image file.
    The endpoint will return a JSON response with the predictions for the image.

    Python example:

    ```
    import requests

    url = 'http://localhost:8000/predict'   # replace with your url
    image_path = 'image1.jpg'               # replace with your image path

    results = requests.post(url, files=[('file', open(image_path, 'rb'))])
    print(results.json())
    ```

    Which should print something like following:

    **[{"class_index": 0, "class_name": "animal", "x": 10.0, "y": 20.0, "width": 1000.2, "height": 125.3, "confidence": 0.20}]**

    Note that the x,y origin is the top left corner in pixel coordinates. The width and height are also in pixels.
    You can use the **confidence_threshold** parameter to control the confidence score threshold for the predictions.

    Want to try this? Click on the **Try it out** button and upload an image using the **Choose File** button in the *Request body* section.
    """

    try:
        contents = file.file.read()  # bytes
        imput_image, resize_factor = scale_image(contents)
        results = model(imput_image)

        # Convert the results to a pandas dataframe, drop low confidence scores and convert back to JSON
        results = results.pandas().xyxy[0]
        results.drop(results[results.confidence < confidence_threshold].index, inplace=True)
        results.rename(columns={"class": "class_id", "name": "class_name", "xmin": "x", "ymin": "y"}, inplace=True)

        # Output in record format xmin, ymin, width, height as integers for each detection
        results["width"] = (results["xmax"] - results["x"]) / resize_factor
        results["height"] = (results["ymax"] - results["y"]) / resize_factor
        results["x"] = results["x"] / resize_factor
        results["y"] = results["y"] / resize_factor
        results.drop(columns=["xmax", "ymax"], inplace=True)
        return results.to_dict(orient="records")
    except Exception as e:
        print(e)
        return {"message": f"Error uploading the file {e}"}
    finally:
        file.file.close()

    return {"message": "OK"}


@app.post("/image", status_code=status.HTTP_200_OK)
async def predict_to_image(file: UploadFile = File(...), confidence_threshold: float = 0.01):
    """
    Upload an image file and return the predictions on the image.

    Want to try this? Click on the **Try it out** button and upload an image using the **Choose File** button in the *Request body* section.
    """
    try:
        contents = file.file.read()
        im = Image.open(io.BytesIO(contents)).convert("RGB")
        input_image, resize_factor = scale_image(contents)
        model.conf = confidence_threshold
        results = model(input_image)
        results.imgs = [np.array(im)]  # replace with original image
        # Get the results from the torch tensor to a numpy array
        results.xyxy[0] = results.xyxy[0].cpu().clone()
        # Scale the bounding boxes to the original image size
        results.xyxy[0][:, :4] = results.xyxy[0][:, :4] / resize_factor
        results.render()  # save the results with boxes and labels
        bytes_io = io.BytesIO()
        img_base64 = Image.fromarray(results.imgs[0])
        img_base64.save(bytes_io, format='PNG')
    except Exception as e:
        print(e)
        return {"message": f"Error uploading the file {e}"}
    finally:
        file.file.close()

    return Response(content=bytes_io.getvalue(), media_type="image/png")
