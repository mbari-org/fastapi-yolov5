import os
from pathlib import Path
from urllib.parse import urlparse

import boto3 as boto3
import torch
from PIL import Image
import io

# Maximum size of any YOLOv5 models
MAX_IMAGE_SIZE = 1024


def load_yolov5():
    print("Loading model...")
    model_labels = None

    # Check if the model path is specified in the environment variable MODEL_PATH
    # If not, use the default model path
    if os.getenv("MODEL_PATH") is None:
        print("MODEL_PATH environment variable not found, using default model path")
        model_path = Path("model/best.pt")
    else:
        print(f"MODEL_PATH environment variable found {os.getenv('MODEL_PATH')}")

        # If the path is a s3 path, download the model to the existing model path model_custom/best.pt
        # S3 paths are in the format s3://bucket-name/path/to/model/
        model_path_p = urlparse(os.getenv("MODEL_PATH"))

        # Create the model path if it doesn't exist
        model_base_path = Path("model_custom")
        model_base_path.mkdir(parents=True, exist_ok=True)

        # If the model path is a s3 path, download the model
        if model_path_p.scheme == "s3":
            s3_client = boto3.client('s3')
            try:
                model_path = model_base_path / "best.pt"
                label_path = model_base_path / "labels.txt"

                # If the model has a netloc and path, download the model
                # netloc is the bucket name
                # path is the path to the model (and labels.txt)
                # Example: s3://bucket-name/path/to/model/
                if model_path_p.netloc and model_path_p.path:
                    print(f"Downloading model from s3://{model_path_p.netloc}{model_path_p.path}best.pt")
                    s3_client.download_file(model_path_p.netloc, f"{model_path_p.path.lstrip('/')}best.pt", model_path.as_posix())
                    s3_client.download_file(model_path_p.netloc, f"{model_path_p.path.lstrip('/')}labels.txt", label_path.as_posix())
                elif model_path_p.netloc:
                    print(f"Downloading model from s3://{model_path_p.netloc}best.pt")
                    s3_client.download_file(model_path_p.netloc, 'best.pt', model_path.as_posix())
                    s3_client.download_file(model_path_p.netloc, 'labels.txt', label_path.as_posix())

                print(f"Model and labels downloaded to {model_path}")
            except Exception as e:
                print(f"Error downloading model and labels: {e}")
                exit(1)
        else:
            model_path = Path(os.getenv("MODEL_PATH")) / "best.pt"
            label_path = Path(os.getenv("MODEL_PATH")) / "labels.txt"

        if not model_path.exists():
            print(f"Model path does not exist: {model_path}")
            exit(1)

        if not label_path.exists():
            print(f"Label path does not exist: {label_path}")
            exit(1)

    print(f"Model path: {model_path}")

    model = torch.hub.load('yolov5', 'custom', path=model_path.as_posix(), source='local')  # local repo
    model.conf = 0.01

    global MAX_IMAGE_SIZE
    # Set the maximum image size based on the model input size (first layer)
    first_layer = next(model.parameters())
    MAX_IMAGE_SIZE = first_layer.shape[1:]

    if model_labels:
        print(f"Loading class labels from {label_path}")
        with label_path.open('r') as f:
            class_labels = f.read().splitlines()
            print(f"Class labels: {class_labels}")

        model.classes = class_labels

    print(f"Model loaded...")
    return model


def scale_image(bytes_images, max_size=MAX_IMAGE_SIZE):
    input_image = Image.open(io.BytesIO(bytes_images)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(max_size / width, max_size / height)
    if resize_factor == 1.0:
        return input_image
    resized_image = input_image.resize(
        (
            int(input_image.width * resize_factor),
            int(input_image.height * resize_factor),
        )
    )
    return resized_image
