from typing import List

from fastapi import APIRouter, UploadFile, File, Depends
import file.controllers as file_controller
import level.controllers as level_controller
from decorators import proto_resp
from level.models import Level
from file.models import File as FileT

from level.views import LevelMetaDataOut, LevelMetaDataCreate, LevelMetaDatasOut
from user.controllers import get_current_active_user
from user.views import UserOut

router = APIRouter()


@router.post("/", tags=["level"])
@proto_resp
async def upload_level(create: LevelMetaDataCreate = Depends(), levelFiles: UploadFile = File(...), current_user: UserOut = Depends(get_current_active_user)):
    file: FileT = await file_controller.upload_file(levelFiles)
    level: Level = level_controller.add_level(create)
    level_controller.add_file_to_level(file.id, level.ulid)
    level_controller.add_level_download(level.ulid)
    level_controller.add_user_to_level(current_user.id, level.ulid)
    return LevelMetaDataOut.from_orm(level)



@router.get("/all", tags=["level"])
@proto_resp
async def get_all_level_meta_datas():
    metaDatas: List[Level] = level_controller.get_levels()
    l = LevelMetaDatasOut(levels = metaDatas)
    return l

@router.delete("/")
async def remove_level(ulid: int,_UserOut = Depends(get_current_active_user)):
    level_controller.remove_level(ulid)



@router.get("/", tags=["level"])
@proto_resp
async def get_level_meta_data(ulid: int):
    metaData = level_controller.get_level(ulid)
    return LevelMetaDataOut.from_orm(metaData)


@router.get("/download", tags=["level"])
@proto_resp
async def download_level(ulid: int):
    level_controller.increment(ulid)
    file: File = level_controller.get_files_of_level(ulid)[0]
    f = await file_controller.download_file(file.id)
    return f
