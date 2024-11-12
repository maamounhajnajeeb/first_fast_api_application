from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello, world!"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# with types
@app.get("/typed_items/{item_id}")
async def read_typed_item(item_id: int):
    return {"item_id": item_id}


# the order of these two functions are important
# hint: try switching functions places and call urls before and after, see the result
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user id"}

@app.get("/users/{user_id}")
async def read_user_me(user_id: int):
    return {"user_id": user_id}


# Enum for fixed (predefined) values
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # note: model_name must be one of those: ['alexnet', 'resnet', 'lenet']
    
    # Comparing between enumeration members
    if model_name is ModelName.alexnet:
        # You can return enum members from your path operation directly
        # They will be converted to their corresponding values (strings in this case) before returning them to the client
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # get the enumeration value with .value
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Path convertor
# In this case, the name of the parameter is file_path, and the last part, :path
# tells it that the parameter should match any path.
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Query Parameters
