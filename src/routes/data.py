from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController, ProcessController
from models import ResponseStatus
from .schemes.data import ProcessRequest
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
    
    # Validate uploaded file
    is_valid, message = data_controller.validate_uploaded_file(file = file)
    
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": message}
        )
    
    # Generate a unique filename
    project_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_file_name(
        filename=file.filename, 
        project_id=project_id)
    
    # Save the file asynchronously (chunks)
    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE_BYTES):  # Read file in chunks
                await out_file.write(chunk)
    
    except Exception as e:
        logger.error(f"Error uploading file {file.filename}: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseStatus.FILE_UPLOAD_FAILURE.value}
        )

    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": message,
                 "file_id": file_id}
    )


@data_router.post("/process/{project_id}")
async def process_data(project_id: str, request: ProcessRequest):
    
    file_id = request.file_id
    chunk_size = request.chunk_size
    overlap = request.overlap
    # do_reset = request.do_reset

    process_controller = ProcessController(project_id=project_id)
    chunks = process_controller.process_file_content(
        file_id=file_id, 
        chunk_size=chunk_size, 
        overlap=overlap
    )

    if chunks is None or len(chunks) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseStatus.PROCESSING_FAILURE.value,
                     "num_chunks": len(chunks)
                     }
        )

    return chunks