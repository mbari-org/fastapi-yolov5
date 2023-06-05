# ================================================================
#  Docker image for fastapi-yolov5
#  ================================================================
FROM ubuntu:20.04
LABEL maintainer="Danelle Cline dcline@mbari.org"
ARG IMAGE_URI=mbari/fastapi-yolov5

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y git \
	&& apt-get install -y build-essential \
	&& apt-get install -y python3.8 \
	&& apt-get install -y python3-pip \
	&& apt-get install -y libgl1-mesa-glx \
	&& apt-get install -y libglib2.0-0 \
	&& apt-get install -y libncurses6

ENV WORKERS_PER_CORE=4
ENV MAX_WORKERS=24
ENV LOG_LEVEL="warning"
ENV TIMEOUT="200"

## force stdin, stdout and stderr to be unbuffered to log to cloudwatch
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8

## setup virtualenv
RUN pip install virtualenv
RUN virtualenv /env -p python3
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

ENV PYTHONPATH=/src
WORKDIR /src/app

COPY ./requirements.txt /src/requirements.txt
COPY ./app /src/app
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt && pip install --no-cache-dir python-multipart && pip install --no-cache-dir --upgrade -r /src/app/yolov5/requirements.txt
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]