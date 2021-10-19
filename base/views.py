from datetime import datetime
from fastapi import UploadFile
import google.protobuf.message

from pydantic import BaseModel


class Request(BaseModel):
    proto_resp: bool = False
    class Config:
        orm_mode = True


class Response(BaseModel):

    class Config:
        orm_mode = True