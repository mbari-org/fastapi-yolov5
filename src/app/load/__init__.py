import torch
from PIL import Image
import io

def load_yolov5():
    print("Loading model...")
    # local best.pt
    model = torch.hub.load('yolov5', 'custom', path='model/best.pt', source='local')  # local repo
    model.conf = 0.10
    print(f"Model loaded...")
    return model


def scale_image(bytes_images, max_size=1024):
    input_image = Image.open(io.BytesIO(bytes_images)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(max_size / width, max_size / height)
    print(f"width: {width}, height: {height} resize_factor: {resize_factor}")
    if resize_factor == 1.0:
        return input_image
    resized_image = input_image.resize(
        (
            int(input_image.width * resize_factor),
            int(input_image.height * resize_factor),
        )
    )
    return resized_image
