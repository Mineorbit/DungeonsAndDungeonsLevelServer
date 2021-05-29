from datetime import datetime

from file.models import File
from level.models import Level, LevelFile, UserLevel, Utility
from level.views import LevelCreate
from util import SessionMaker


def add_level(create: LevelCreate):
    session = SessionMaker()
    level = Level(
        name=create.name,
        upload_date=datetime.today(),
        description=create.description
    )
    session.add(level)
    session.commit()
    _lid = level.ulid
    return level

def add_file_to_level(f_id: int, l_id: int):
    session = SessionMaker()
    levelFile = LevelFile(
        level_id = l_id,
        file_id = f_id
    )
    session.add(levelFile)
    session.commit()
    _lf = levelFile.file_id


def add_user_to_level(u_id: int, l_id: int):
    session = SessionMaker()
    userLevel = UserLevel(
        level_id = l_id,
        user_id = u_id
    )
    session.add(userLevel)
    session.commit()
    _lu = userLevel.user_id


def get_level(ulid: int):
    session = SessionMaker()
    level = session.query(Level).filter(Level.ulid == ulid).first()
    return level


def get_files_of_level(ulid: int, types = [Utility.LEVELDATA]):
    session = SessionMaker()
    files = session.query(LevelFile, File).filter(LevelFile.file_id == File.id).filter(LevelFile.level_id == ulid).\
        filter(LevelFile.type.in_(types)).with_entities(File).all()
    return files



