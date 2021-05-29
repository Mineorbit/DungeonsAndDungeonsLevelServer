from fastapi import APIRouter, UploadFile, File, Depends
import file.controllers as file_controller
import level.controllers as level_controller
from level.models import Level
from file.models import File as FileT

from level.views import LevelOut, LevelCreate
from user.controllers import get_current_active_user
from user.views import UserOut

router = APIRouter()


@router.post("/", tags=["level"])
async def upload_level(create: LevelCreate = Depends(), levelFiles: UploadFile = File(...), current_user: UserOut = Depends(get_current_active_user)):
    file: FileT = await file_controller.upload_file(levelFiles)
    level: Level = level_controller.add_level(create)
    level_controller.add_file_to_level(file.id,level.ulid)
    level_controller.add_user_to_level(current_user.id,level.ulid)
    return LevelOut.from_orm(level)



@router.get("/all", tags=["level"])
async def get_all_level_meta_datas():
    metaDatas = level_controller.get_levels()
    return metaDatas


@router.get("/", tags=["level"])
async def get_level_meta_data(ulid: int):
    metaData = level_controller.get_level(ulid)
    return metaData


@router.get("/download", tags=["level"])
async def download_level(ulid: int):
    file: File = level_controller.get_files_of_level(ulid)[0]
    f = await file_controller.download_file(file.id)
    return f
