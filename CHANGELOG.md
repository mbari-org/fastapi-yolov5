# FastAPI-YOLOv5  Changelog

# [1.1.0](https://github.com/mbari-org/fastapi-yolov5/compare/v1.0.1...v1.1.0) (2023-08-14)


### Features

* support model checkpoint and labels with unique names ([4065501](https://github.com/mbari-org/fastapi-yolov5/commit/4065501f4286e8d15fb1952cdb51f85ba7e0e03d))

## [1.0.1](https://github.com/mbari-org/fastapi-yolov5/compare/v1.0.0...v1.0.1) (2023-08-13)


### Bug Fixes

* correct docker build for 3.10 as needed for current design ([0608b74](https://github.com/mbari-org/fastapi-yolov5/commit/0608b74cfa5ec83c89b45ddb35742e4b6f15b0db))

# 1.0.0 (2023-08-13)


### Bug Fixes

* correct formatting of cdk.json ([1bf3bfb](https://github.com/mbari-org/fastapi-yolov5/commit/1bf3bfbce9cccec476d3466748d3980fac07e193))
* entrypoint for docker image ([042485b](https://github.com/mbari-org/fastapi-yolov5/commit/042485b848a99011038045575bd717a15334d0dd))


### Features

* added MBARI security group and health check ([7889a71](https://github.com/mbari-org/fastapi-yolov5/commit/7889a714f80adfdd5be277c01b63ba6eb163f9c0))
* added secrets and cloud model load to cdk ([6016e3c](https://github.com/mbari-org/fastapi-yolov5/commit/6016e3c2f09ec6b4ba462b442059f3325a00d135))
* added support for loading a custom model via env MODEL_PATH either local or S3 ([59620b3](https://github.com/mbari-org/fastapi-yolov5/commit/59620b310c96fc8e44d0010ce46ac358ea075823))
* initial commit ([5fdae39](https://github.com/mbari-org/fastapi-yolov5/commit/5fdae3908e6076844dd9bd5c5a1f15b34498a281))
* Megadetector default, added description, output png instead of png, better pandas record handling and fixed ingress rules in CDK to force MBARI only access ([70a9081](https://github.com/mbari-org/fastapi-yolov5/commit/70a9081bf18594ecd763014c937faf9b7d8affa2))
* switch to yaml config of stack ([bc08b56](https://github.com/mbari-org/fastapi-yolov5/commit/bc08b56597a00b9c9f35340b547a05a69406a419))
* trigger release ([e483963](https://github.com/mbari-org/fastapi-yolov5/commit/e483963a5ebf9352602a7fdae19a80eb5c0cd398))


### Performance Improvements

* added autoscaling ([58d3a60](https://github.com/mbari-org/fastapi-yolov5/commit/58d3a60ffd011448381dae0681dd69e115c44e14))
* reduce  conf to 0.1 ([ad1dcb8](https://github.com/mbari-org/fastapi-yolov5/commit/ad1dcb86d48bcf1a136eb565ee36d9179088acdf))
* reduce conf default to .01 ([49ee785](https://github.com/mbari-org/fastapi-yolov5/commit/49ee7856c7ce6367f8482a9df3359fd2ab328d46))

# [1.5.0](https://github.com/mbari-org/fastapi-yolov5/compare/v1.4.1...v1.5.0) (2023-06-22)


### Features

* switch to yaml config of stack ([7fe642c](https://github.com/mbari-org/fastapi-yolov5/commit/7fe642c6ac0f56ea96100c687470efd2c660ac73))

## [1.4.1](https://github.com/mbari-org/fastapi-yolov5/compare/v1.4.0...v1.4.1) (2023-06-14)


### Bug Fixes

* correct formatting of cdk.json ([f152fe7](https://github.com/mbari-org/fastapi-yolov5/commit/f152fe7f09dfaf37859c3d767458ae7c956a7dc6))

# [1.4.0](https://github.com/mbari-org/fastapi-yolov5/compare/v1.3.2...v1.4.0) (2023-06-14)


### Features

* trigger release ([9d3edcc](https://github.com/mbari-org/fastapi-yolov5/commit/9d3edcc7e3bfd4da965aa853fd47571cbfe17f38))

## [1.3.2](https://github.com/mbari-org/fastapi-yolov5/compare/v1.3.1...v1.3.2) (2023-06-13)


### Performance Improvements

* added autoscaling ([80c4623](https://github.com/mbari-org/fastapi-yolov5/commit/80c462391ea9ee88a20a1fecc6467906ff060a81))

## [1.3.1](https://github.com/mbari-org/fastapi-yolov5/compare/v1.3.0...v1.3.1) (2023-06-13)


### Performance Improvements

* reduce conf default to .01 ([8936740](https://github.com/mbari-org/fastapi-yolov5/commit/8936740eb2fd47542cb84ce785e8bb477a002e57))

# [1.3.0](https://github.com/mbari-org/fastapi-yolov5/compare/v1.2.0...v1.3.0) (2023-06-13)


### Features

* added secrets and cloud model load to cdk ([7a4dc23](https://github.com/mbari-org/fastapi-yolov5/commit/7a4dc236db02c9a9a3c52a6e6e06b9e2b794e365))

# [1.2.0](https://github.com/mbari-org/fastapi-yolov5/compare/v1.1.1...v1.2.0) (2023-06-12)


### Features

* added support for loading a custom model via env MODEL_PATH either local or S3 ([802e3e9](https://github.com/mbari-org/fastapi-yolov5/commit/802e3e9910bd10c58118fa48bdafca1a124503de))

## [1.1.1](https://github.com/mbari-org/fastapi-yolov5/compare/v1.1.0...v1.1.1) (2023-06-11)


### Performance Improvements

* reduce  conf to 0.1 ([d952f45](https://github.com/mbari-org/fastapi-yolov5/commit/d952f45a5064ce5c758ff228b9467eb67158d71c))

# [1.1.0](https://github.com/mbari-org/fastapi-yolov5/compare/v1.0.0...v1.1.0) (2023-06-10)


### Features

* added MBARI security group and health check ([01a08c0](https://github.com/mbari-org/fastapi-yolov5/commit/01a08c0a5ea58a19acb1f152f77b08f7cfab17a7))

# FastAPI-YOLOv5 Changelog

# 1.0.0 (2023-06-07)


### Bug Fixes

* entrypoint for docker image ([042485b](https://github.com/mbari-org/fastapi-yolov5/commit/042485b848a99011038045575bd717a15334d0dd))


### Features

* initial commit ([5fdae39](https://github.com/mbari-org/fastapi-yolov5/commit/5fdae3908e6076844dd9bd5c5a1f15b34498a281))
