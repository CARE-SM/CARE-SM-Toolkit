from fastapi import FastAPI, Response, status
# import pandas
import uvicorn
import os
from toolkit.main import Toolkit

app = FastAPI()
folder = os.getcwd() + "/data/"
@app.get("/")
async def api_running():
    return {'message': 'API running'}

@app.post("/toolkit")
async def csv_transformation_by_caresm_toolkit(response: Response):
    toolkit_instance = Toolkit()
    toolkit_instance.whole_method(folder_path=folder)
    response.status_code = status.HTTP_200_OK
    if response.status_code == 200:
        return {response.status_code: "Structural Transformation done"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)