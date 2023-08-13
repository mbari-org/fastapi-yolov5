# !/usr/bin/env python
__author__ = "Danelle Cline"
__copyright__ = "Copyright 2023, MBARI"
__credits__ = ["MBARI"]
__license__ = "GPL"
__maintainer__ = "Danelle Cline"
__email__ = "dcline at mbari.org"
__doc__ = '''

Test the prediction endpoints

@author: __author__
@status: __status__
@license: __license__
'''
import tempfile
from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app
from PIL import Image
from PIL import ImageChops


# Get the path of this file
path = Path(__file__)

# Get the path of a test image and the expected content after inference
image_path = path.parent / 'midwater.png'
image_path_detect = path.parent / 'midwater_predict_to_image.png'

# Create a test client
client = TestClient(app)


def test_predict():
    print('Test that the predict endpoint returns 200')
    response = client.post('/predict', files=[('file', open(image_path.as_posix(), 'rb'))])
    print(response)
    assert response.status_code == 200


def test_predict_detections():
    print('Test that the predict endpoint returns 7 boxes')
    response = client.post('/predict', files=[('file', open(image_path.as_posix(), 'rb'))])
    print(response)
    assert response.status_code == 200
    detections = response.json()
    assert len(detections) == 7


def test_predict_image_status():
    print('Test that the inference to image endpoint returns a 200 status code')
    response = client.post('/image', files=[('file', open(image_path.as_posix(), 'rb'))])
    print(response)
    assert response.status_code == 200


def test_image_content():
    print('Test that the inference to image endpoint image matches the expected image')
    response = client.post('/image', files=[('file', image_path.open('rb'))])

    with tempfile.TemporaryDirectory() as temp_dir:
        image_out = Path(temp_dir) / 'midwater_predict_to_image.png'

        with image_out.open('wb') as f:
            f.write(response.content)

        image_one = Image.open(image_out.as_posix())
        image_two = Image.open(image_path_detect.as_posix())

        diff = ImageChops.difference(image_one, image_two)
        assert diff.getbbox()