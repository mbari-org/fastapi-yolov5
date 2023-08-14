# Development notes
 
## Install for local development with

```shell
conda activate fastapi-yolov5
export PYTHONPATH=$PWD/src
cd src/app && uvicorn main:app --reload
```
 
This will start the server on port 8000.  

## Testing

Run the pytest tests from the root directory with

```shell
pytest
```