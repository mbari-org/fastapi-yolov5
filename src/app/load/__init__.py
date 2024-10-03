import os
from pathlib import Path
from urllib.parse import urlparse

import boto3 as boto3
import torch
from PIL import Image
import io

MODEL_INPUT_SIZE = 1280
MODEL_DESCRIPTION = "Megadetector"


def download_from_s3(s3_path: str, local_path: str) -> Path:
    """
    Download a file from S3 and save it to the local path
    :param s3_path: S3 path to the file
    :param local_path: Local path to save the file
    :return: Path to the downloaded file
    """
    s3_parsed = urlparse(s3_path)
    s3 = boto3.client('s3')
    try:
        model_path = local_path / Path(s3_parsed.path).name
        print(f"Downloading model from {s3_path}")
        s3.download_file(s3_parsed.netloc, s3_parsed.path.lstrip('/'), model_path.as_posix())
        print(f"Downloaded to {model_path}")
        return model_path
    except Exception as e:
        print(f"Error downloading model and labels: {e}")
        exit(1)

def load_yolov5():
    """
    Load the YOLOv5 model either from a local file or from S3
    :return: model, description
    """
    print("Loading model...")
    global MODEL_INPUT_SIZE, MODEL_DESCRIPTION, MODEL_WEIGHTS, MODEL_LABELS

    # Check if the model input size is specified in the environment variable MODEL_INPUT_SIZE
    # If not, use the default image size
    if os.getenv("MODEL_INPUT_SIZE") is None:
        print(f"MODEL_INPUT_SIZE environment variable not found, using default image size {MODEL_INPUT_SIZE}")
    else:
        print(f"MODEL_INPUT_SIZE environment variable found {os.getenv('MODEL_INPUT_SIZE')}")
        MODEL_INPUT_SIZE = int(os.getenv("MODEL_INPUT_SIZE"))

    if os.getenv("MODEL_DESCRIPTION") is None:
        print(f"MODEL_DESCRIPTION environment variable not found, using default model description {MODEL_DESCRIPTION}")
    else:
        print(f"MODEL_DESCRIPTION environment variable found {os.getenv('MODEL_DESCRIPTION')}")
        MODEL_DESCRIPTION = os.getenv("MODEL_DESCRIPTION")

    # Default model
    path = Path(__file__).parent.parent / "model"
    model_path = path / 'best.pt'
    label_path = path / 'labels.txt'

    # Create a directory to store the custom model and labels
    model_base_path = Path("model_custom")
    model_base_path.mkdir(parents=True, exist_ok=True)

    # Check if custom model data is specified in the environment variables MODEL_WEIGHTS and MODEL_LABELS
    for e in ["MODEL_WEIGHTS", "MODEL_LABELS"]:
        env_path = os.getenv(e)
        if env_path is None:
            print(f"{e} environment variable not found, using default")
            path = Path(__file__).parent.parent / "model"
            if 'MODEL_WEIGHTS':
                model_path = path / 'best.pt'
            if 'MODEL_LABELS':
                label_path = path / 'labels.txt'
        else:
            print(f"{e} environment variable found {env_path}")
            if urlparse(env_path).scheme == "s3":
                if e == "MODEL_WEIGHTS":
                    model_path = download_from_s3(env_path, model_base_path)
                if e == "MODEL_LABELS":
                    label_path = download_from_s3(env_path, model_base_path)

    if not model_path.exists():
        print(f"Model path does not exist: {model_path}")
        exit(1)

    if not label_path.exists():
        print(f"Label path does not exist: {label_path}")
        exit(1)

    print(f"Model: {model_path}")
    print(f"Labels: {label_path}")

    model = torch.hub.load(f'{Path(__file__).parent.parent}/yolov5', 'custom', path=model_path.as_posix(),
                           source='local')  # local repo
    model.conf = 0.01

    # If GPU is available, use it
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device).eval()

    print(f"Loading class labels from {label_path}")
    with label_path.open('r') as f:
        class_labels = f.read().splitlines()
        print(f"Class labels: {class_labels}")
        model.names = class_labels

    print("Model loaded. Ready to process images.")
    return model, MODEL_DESCRIPTION


def scale_image(bytes_images):
    global MODEL_INPUT_SIZE
    input_image = Image.open(io.BytesIO(bytes_images)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(MODEL_INPUT_SIZE / width, MODEL_INPUT_SIZE / height)
    if resize_factor == 1.0:
        return input_image, 1.0
    resized_image = input_image.resize(
        (
            int(input_image.width * resize_factor),
            int(input_image.height * resize_factor),
        )
    )
    return resized_image, resize_factor


if __name__ == "__main__":
    os.environ["MODEL_WEIGHTS"] = "s3://tarun-901103-test-bucket/model_weights/megafish_ROV_weights.pt"
    os.environ["MODEL_LABELS"] = "s3://tarun-901103-test-bucket/model_weights/megafish_ROV_labels.txt"
    load_yolov5()