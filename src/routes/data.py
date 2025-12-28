from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseStatus
import logging
import aiofiles

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(file: UploadFile, project_id: str,
                       app_settings: Settings = Depends(get_settings)):
    
    data_controller = DataController()
    
    is_valid, message = data_controller.validate_uploaded_file(file = file)
    
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": message}
        )
    
    project_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_file_name(
        filename=file.filename, 
        project_id=project_id)
    
    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE_BYTES):  # Read file in chunks
                await out_file.write(chunk)
    
    except Exception as e:
        logger.error(f"Error uploading file {file.filename}: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": ResponseStatus.FILE_UPLOAD_FAILED.value}
        )

    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": message,
                 "file_id": file_id}
    )