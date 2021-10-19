from datetime import datetime

from file.models import File
import file.controllers as file_controller
from level.models import Level, LevelFile, UserLevel, Utility
from level.views import LevelMetaDataCreate
from util import SessionMaker

from level.models import LevelDownload


def add_level(create: LevelMetaDataCreate):
    session = SessionMaker()
    level = Level(
        name=create.name,
        upload_date=datetime.today(),
        description=create.description
    )
    session.add(level)
    session.commit()
    lid = level.ulid

    session.expunge_all()
    session.commit()
    session.close()
    return level


def add_level_download(l_id: int):
    session = SessionMaker()
    level_download = LevelDownload(
        level_id=l_id,
        downloads=0

    )
    session.add(level_download)
    session.commit()


def add_file_to_level(f_id: int, l_id: int):
    session = SessionMaker()
    levelFile = LevelFile(
        level_id = l_id,
        file_id = f_id
    )
    session.add(levelFile)
    session.commit()
    _lf = levelFile.file_id


def remove_level(ulid: int):
    session = SessionMaker()
    files = session.query(LevelFile, File).filter(LevelFile.file_id == File.id).filter(LevelFile.level_id == ulid).\
        with_entities(File).all()
    for f in files:
        file_controller.remove_file(f.id)
    session.query(LevelFile).filter(LevelFile.level_id == ulid).delete()
    session.query(Level).filter(Level.ulid == ulid).delete()
    session.commit()


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


def get_levels():
    session = SessionMaker()
    levels = session.query(Level).all()
    return levels


def increment(ulid: int):
    session = SessionMaker()
    level_download: LevelDownload = session.query(LevelDownload).filter(LevelDownload.level_id == ulid).first()
    level_download.downloads = level_download.downloads + 1
    session.commit()


def get_files_of_level(ulid: int, types=[Utility.LEVELDATA]):
    session = SessionMaker()
    files = session.query(LevelFile, File).filter(LevelFile.file_id == File.id).filter(LevelFile.level_id == ulid).\
        filter(LevelFile.type.in_(types)).with_entities(File).all()
    return files



