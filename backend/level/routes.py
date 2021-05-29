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
    level_controller.add_file_to_level(file.id,level.id)
    level_controller.add_user_to_level(current_user.id,level.id)
    return LevelOut.from_orm(level)

