import requests

# TODO: refactor this into a test suite
# Test the endpoint export to image file
image_path = "midwater.png"
endpoint = 'localhost:3000'

url = f"http://{endpoint}/predict_to_json"  # Replace with the URL of your FastAPI endpoint

response = requests.post(url, files=[('file', open(image_path, 'rb'))])

# Print the response
print(response)
print(response.json())

# from PIL import Image, ImageDraw
# import pandas as pd
# Open the image
# image = Image.open(image_path)
#
# # Create a draw object
# draw = ImageDraw.Draw(image)

# Display the boxes on the image

# # Iterate over the boxes
# detections = pd.DataFrame(response_json['result'])
# for i, box in detections.iterrows():
#         # Draw the bounding box
#         print(box)
#         box_ = int(box['xmin']), int(box['ymin']), int(box['xmax']), int(box['ymax'])
#         draw.rectangle(box_, outline="red", width=3)
#
# # Display the image
# image.show()

url = f"http://{endpoint}/predict_to_img"  # Replace with the URL of your FastAPI endpoint

response = requests.post(url, files=[('file', open(image_path, 'rb'))])

# Print the response
print(response)

# The image is returned as a byte string
# You can save the image to a file like this:
with open("midwater_detect.png", "wb") as f:
        f.write(response.content)