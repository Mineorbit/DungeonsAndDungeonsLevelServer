from fastapi import APIRouter, File, UploadFile
import file.controllers as file_controller
from file.views import FileOut

router = APIRouter()


# @router.post("/", tags=["file"])
# async def upload(file: bytes = File(..)):


@router.post("/", tags=["file"])
async def upload_file(file: UploadFile = File(...)):
    file = await file_controller.upload_file(file)
    return FileOut.from_orm(file)


@router.get("/{file_id}", tags=["file"])
async def download_file(file_id: int):
    f = await file_controller.download_file(file_id)
    return f