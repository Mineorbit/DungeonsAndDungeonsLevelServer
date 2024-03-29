from datetime import datetime

import aiofiles
import fastapi
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from aiofiles import os
import os.path
from os import path

from starlette.responses import FileResponse

from file.models import File
from util import SessionMaker

import config


async def upload_file(in_file: fastapi.UploadFile):
    session = SessionMaker()
    file = File(
        name = in_file.filename,
        type = in_file.content_type,
        upload_date = datetime.today()
    )
    session.add(file)
    session.commit()
    if(not path.exists(config.PERMANENT_DATA)):
        os.mkdir(config.PERMANENT_DATA)
    file_location = config.PERMANENT_DATA + "/" + str(file.id)
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)

    session.close()
    return file


def remove_file(file_id: int):
    try:
        os.remove(config.PERMANENT_DATA + "/" + str(file_id))
    except Exception:
        pass
    session = SessionMaker()
    session.query(File).filter(File.id == file_id).delete()
    session.commit()
    session.close()


async def download_file(file_id: int):
    session = SessionMaker()
    f: File = session.query(File).filter(File.id == file_id).first()
    session.close()
    if f is None:
        raise HTTPException(status_code=404, detail="File not found") 
    return FileResponse(config.PERMANENT_DATA + "/" + str(f.id), media_type=f.type, filename=f.name)

