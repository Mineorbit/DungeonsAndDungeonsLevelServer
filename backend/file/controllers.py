from datetime import datetime

import aiofiles
import fastapi
from aiofiles import os
import os.path
from os import path

from starlette.responses import FileResponse

from file.models import File
from util import SessionMaker


file_path = "uploaded_files"


async def upload_file(in_file: fastapi.UploadFile):
    session = SessionMaker()
    file = File(
        name = in_file.filename,
        type = in_file.content_type,
        upload_date = datetime.today()
    )
    session.add(file)
    session.commit()
    if(not path.exists(file_path)):
        os.mkdir(file_path)
    file_location = file_path+"/"+str(file.id)
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)
    return file


async def download_file(file_id: int):
    session = SessionMaker()
    f: File = session.query(File).filter(File.id == file_id).first()
    return FileResponse(file_path+"/"+str(f.id), media_type=f.type, filename=f.name)

