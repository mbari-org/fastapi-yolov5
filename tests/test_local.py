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

url = f"http://{endpoint}/predict_to_img"  # Replace with the URL of your FastAPI endpoint

response = requests.post(url, files=[('file', open(image_path, 'rb'))])

# Print the response
print(response)

# The image is returned as a byte string
# You can save the image to a file like this:
with open("midwater_detect.png", "wb") as f:
        f.write(response.content)