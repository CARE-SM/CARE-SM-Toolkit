from fastapi import FastAPI, Response, status
import pandas
import uvicorn
import os
from toolkit.main import Toolkit

app = FastAPI()

@app.get("/")
async def api_running():
    return {'message': 'API running'}


@app.post("/toolkit")
async def csv_transformation_by_caresm_toolkit(response: Response):
    current_dir = os.getcwd()
    toolkit = Toolkit()
    transform = toolkit.whole_quality_control(input_data= current_dir + "/data/preCARE.csv")
    transform.to_csv (current_dir + "/data/CARE.csv", index = False, header=True)
    response.status_code = status.HTTP_200_OK
    if response.status_code == 200:
        return {response.status_code:"Structural Transformation done"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)