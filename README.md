
This repository deploys and runs the YOLOv5 model in the Python web framework [FastAPI](https://fastapi.tiangolo.com/) both locally and in AWS.

# Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

# Deploy YOLOv5 locally

This will start the FastAPI server on port 3000.  To start the server, run
```shell
docker-compose up
```

Check the health of the server by going to `http://localhost:3000/health`.  You should see the following response:

```json
{"status":"ok"}
```
 You can now send a POST request to `http://localhost:3000/predict_to_json` with an image file in the body to get a prediction.

```shell
curl -X POST "http://localhost:3000/predict_to_json" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@<path_to_image>"
```
To stop the server, run

```shell
docker-compose down
```


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
curl -X POST "http://FastA-FastA-53HYPWCIRUXS-1905789853.us-west-2.elb.amazonaws.com/predict_to_json" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=tests/midwater.png"
```

## Deploying a custom model locally

To override the default model, you can mount a local directory to the container and set the MODEL_PATH environment variable.
For example, if you have a model in the directory `~/models/best`, you can mount that directory to the container by adding the following to the `docker-compose.yml` file
and the  MODEL_PATH environment variable to the `environment` section of the `app` service:
```yaml
app:
    volumes:
      - ~/models/best:/app/models/best
    environment:
      - MODEL_PATH=/app/models/best
```

The directory should contain the `best.pt` file and the labels file labels.txt for that model.
The labels file should be in the format of one label per line.

```shell
docker-compose up
```

## Deploying a custom model in AWS

To override the default model, upload the `best.pt` file and the labels file `labels.txt` for that model to an S3 bucket.
Specify the S3 bucket in the `MODEL_PATH` environment variable in the `cdk.json` file, then deploy.
The S3 bucket must be in the same region as the ECS cluster

```shell
cdk deploy
```