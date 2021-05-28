import aiofiles as aiofiles
from fastapi import APIRouter, File, UploadFile
import file.controllers as file_controller
import config

router = APIRouter()


# @router.post("/", tags=["file"])
# async def upload(file: bytes = File(..)):




@router.post("/", tags=["file"])
async def upload(file: UploadFile = File(...)):
    await file_controller.handle_upload_file(file)
    return "File uploaded"


@router.get("/{file_id}", tags=["file"])
async def download(file_id: int):
    f = await file_controller.download_file(file_id)
    return f