from fastapi import FastAPI, Response, status
import uvicorn
from pathlib import Path
from toolkit.main import Toolkit
import logging
logger = logging.getLogger(__name__)

app = FastAPI()

folder = Path(__file__).resolve().parent.parent / "data"

@app.get("/")
async def api_running():
    return {'API-status': 'running'}

@app.post("/toolkit", status_code=status.HTTP_200_OK)
async def csv_transformation_by_caresm_toolkit():
    toolkit_instance = Toolkit()

    try:
        toolkit_instance.whole_method(folder_path=str(folder), template_type="OBO")
        logger.info("Structural Transformation completed successfully.")
        return {"message": "Structural Transformation done"}
    except Exception as e:
        return Response(
            content=f"An error occurred: {str(e)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@app.post("/CSV2OBO", status_code=status.HTTP_200_OK)
async def csv_transformation_by_caresm_toolkit():
    toolkit_instance = Toolkit()

    try:
        toolkit_instance.whole_method(folder_path=str(folder), template_type="OBO")
        logger.info("Structural Transformation completed successfully.")
        return {"message": "Structural Transformation done"}
    except Exception as e:
        return Response(
            content=f"An error occurred: {str(e)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@app.post("/CSV2SNOMED", status_code=status.HTTP_200_OK)
async def csv_transformation_by_caresm_toolkit():
    toolkit_instance = Toolkit()

    try:
        toolkit_instance.whole_method(folder_path=str(folder), template_type="SNOMED")
        logger.info("Structural Transformation completed successfully.")
        return {"message": "Structural Transformation done"}
    except Exception as e:
        return Response(
            content=f"An error occurred: {str(e)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
