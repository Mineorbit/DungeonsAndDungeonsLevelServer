from datetime import datetime

from level.models import LevelMetaData
from level.views import LevelCreate
from util import SessionMaker


def add_level(create: LevelCreate, f_id: int, u_id: int):
    session = SessionMaker()
    level = LevelMetaData(
        name=create.name,
        upload_date=datetime.today(),
        file_id=f_id
    )
    session.add(level)
    print(str(level.uniqueGlobalLevelId))
    session.commit()
    _lid = level.uniqueGlobalLevelId
    return level

