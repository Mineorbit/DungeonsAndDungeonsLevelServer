from fastapi import APIRouter, UploadFile, File, Depends
import file.controllers as file_controller
import level.controllers as level_controller

from level.views import LevelOut, LevelCreate
from user.controllers import get_current_active_user
from user.views import UserOut

router = APIRouter()


@router.post("/", tags=["level"])
async def upload_level(create: LevelCreate = Depends(), f: UploadFile = File(...), current_user: UserOut = Depends(get_current_active_user)):
    file = await file_controller.upload_file(f)
    level = level_controller.add_level(create, file.id, current_user.id)
    return LevelOut.from_orm(level)

