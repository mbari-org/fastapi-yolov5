[![MBARI](https://www.mbari.org/wp-content/uploads/2014/11/logo-mbari-3b.png)](http://www.mbari.org)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
![license-GPL](https://img.shields.io/badge/license-GPL-blue)
[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/downloads/)

**fastapi-yolov5** code deploys and runs the YOLOv5 model in the Python web framework [FastAPI](https://fastapi.tiangolo.com/) either locally or in AWS.

It is currently live at https://deepsea-ai.mbari.org/megadetector/docs

# Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

# Deploy YOLOv5 locally

## Clone the repository and create the conda environment
```shell
git clone http://github.com/mbari-org/fastapi-yolov5
cd fastapi-yolov5
conda env create
```

## Download an example model

```shell
cd src/app/models
aws s3 cp --no-sign-request s3://902005-public/models/Megadetector/best.pt .
aws s3 cp --no-sign-request s3://902005-public/models/Megadetector/labels.txt .
```

## Start the FastAPI server

```shell
docker-compose up
```
To stop the server, run
```shell
docker-compose down
```

# Running

## Health Check
Check the health of the server by going to `http://localhost:3000/health`.  You should see the following response:

```json
{"status":"ok"}
```

## Predict to JSON

Send a POST request to `http://localhost:3000/predict` with an image file in the body to get a prediction returned in JSON format.
By default, predictions greater than 0.01 are posted.

```shell
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@tests/midwater.png"
```

# Predict to an image file

Send a POST request to `http://localhost:8000/image` with an image file in the body to get the predictions displayed on an image.
By default, predictions greater than 0.01 are displayed.

```shell
curl -X POST "http://localhost:8000/image" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@tests/midwater.png" -o midwater_detect.png
```

![Image link ](tests/midwater_predict_to_image.png)
 


# Deploy YOLOv5 in AWS

FastAPI deployed with ECS Fargate and exposed with an Application Load Balancer

```shell
cdk bootstrap
cdk deploy
```

You should see at the end the exposed endpoint, e.g. **http://FastA-FastA-53HYPWCIRUXS-1905789853.us-west-2.elb.amazonaws.com** below.


```shell
FastAPIStack: deploying... [1/1]
FastAPIStack: creating CloudFormation changeset...

 ✅  FastAPIStack

✨  Deployment time: 369.74s

Outputs:
FastAPIStack.FastAPIYOLOv5ServiceLoadBalancerDNS68FA283F = FastA-FastA-53HYPWCIRUXS-1905789853.us-west-2.elb.amazonaws.com
FastAPIStack.FastAPIYOLOv5ServiceServiceURL365F19C7 = http://FastA-FastA-53HYPWCIRUXS-1905789853.us-west-2.elb.amazonaws.com
Stack ARN:
arn:aws:cloudformation:us-west-2:975513124282:stack/FastAPIStack/89fcc790-07d4-11ee-924e-02e23803e407

✨  Total time: 377.69s
```

Test this by running a test image through the endpoint

```
curl -X POST "http://FastA-FastA-53HYPWCIRUXS-1905789853.us-west-2.elb.amazonaws.com/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=tests/midwater.png"
```

## Deploying a custom model locally

To override the default model, you can mount a local directory to the container and set the MODEL_PATH environment variable.

For example, if you have a model in the directory `./models/best`, you can mount that directory to the container by adding 
the following to the `docker-compose.yml` file.

```yaml
app:
    volumes:
      - ./models/midwater102:/app/models/best
    environment:
      - MODEL_WEIGHTS=/app/models/best/best.pt
      - MODEL_LABELS=/app/models/best/labels.txt
      - MODEL_DESCRIPTION="Megadetector"
```
 
The labels file should be in the format of one label per line.

```
.
├── models/             # Parent directory for models
│   │
│   ├── midwater102/    # Model directory
│   │   ├── best.pt     #  Model YOLOv5 checkpoint file
│   │   ├── labels.txt  #  Model YOLOv5 labels file

```

```shell
docker-compose up
```

## Deploying a custom model in AWS

To override the default model, upload the `best.pt` file and the labels file `labels.txt` for that model to an S3 bucket.
Specify the S3 bucket in the `MODELPATH` environment variable in the `config.yaml` file.
The S3 bucket must be in the same region as the ECS cluster

```yaml
app:
    environment:
      - MODEL_WEIGHTS=s3://901103-models-deploy/megadetector/best.pt
      - MODEL_LABELS=s3://901103-models-deploy/megadetector/best.pt 
      - MODEL_DESCRIPTION="Megadetector"
```

Deploy the stack with the new configuration

```shell
cdk deploy
```