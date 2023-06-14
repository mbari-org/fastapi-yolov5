# !/usr/bin/env python
__author__ = "Danelle Cline"
__copyright__ = "Copyright 2023, MBARI"
__credits__ = ["MBARI"]
__license__ = "GPL"
__maintainer__ = "Danelle Cline"
__email__ = "dcline at mbari.org"
__doc__ = '''

Run a FastAPI server to serve the YOLOv5 model

@author: __author__
@status: __status__
@license: __license__
'''

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
from app.load import load_yolov5, scale_image
from app import __version__
from PIL import Image
import io
import json

model = load_yolov5()

app = FastAPI(
    title="MBARI YOLOv5 Machine Learning API",
    description="""Predicts localizations in images using YOLOV5;
                    returns results in an image or json""",
    version=__version__,
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


@app.get('/health')
def get_health():
    """
    Health check endpoint
    :return:
        dict(msg='OK')
    """
    return dict(msg='OK')


@app.post("/predict_to_json")
def upload(file: UploadFile = File(...)):
    """
    Upload an image file and return the predictions in JSON format. Only predictions with a confidence > 0.5 are returned. See load_yolov5() for the model configuration.
    :param file:
    :return: {"result": detect_res}
    """
    try:
        contents = file.file.read() # bytes
        imput_image, resize_factor = scale_image(contents)
        results = model(imput_image)
        detect_res = results.pandas().xyxy[0].to_json(orient="records")  # JSON predictions
        detect_res = json.loads(detect_res)
        # Rescale the bounding boxes to the original image size
        for i in range(len(detect_res)):
            print(detect_res[i])
            detect_res[i]["xmin"] = int(detect_res[i]["xmin"] / resize_factor)
            detect_res[i]["xmax"] = int(detect_res[i]["xmax"] / resize_factor)
            detect_res[i]["ymin"] = int(detect_res[i]["ymin"] / resize_factor)
            detect_res[i]["ymax"] = int(detect_res[i]["ymax"] / resize_factor)
        return {"result": detect_res}
    except Exception as e:
        print(e)
        return {"message": f"There was an error uploading the file {e}"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded"}


@app.post("/predict_to_img")
async def predict_to_img(file: UploadFile = File(...)):
    """
    Upload an image file and return the predictions in an image. Only predictions with a confidence > 0.5 are returned. See load_yolov5() for the model configuration.
    :param file:
    :return: binary jpeg image
    """
    try:
        contents = file.file.read()  # bytes
        input_image, _ = scale_image(contents)
        results = model(input_image)
        results.render()  # save the results with boxes and labels
        for img in results.imgs:
            bytes_io = io.BytesIO()
            img_base64 = Image.fromarray(img)
            img_base64.save(bytes_io, format="jpeg")
    except Exception as e:
        print(e)
        return {"message": f"There was an error uploading the file {e}"}
    finally:
        file.file.close()

    return Response(content=bytes_io.getvalue(), media_type="image/jpeg")
