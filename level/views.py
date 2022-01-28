from datetime import datetime
from typing import List

import LevelMetaDataList_pb2
import LevelMetaData_pb2
from base.views import Request, Response


class LevelMetaDataOut(Response):
    ulid: int
    name: str
    upload_date: datetime
    description: str
    availBlue: bool
    availGreen: bool
    availRed: bool
    availYellow: bool

    def to_proto(self):
        levelmetadata = LevelMetaData_pb2.LevelMetaData()
        levelmetadata.uniqueLevelId = self.ulid
        levelmetadata.FullName = self.name
        levelmetadata.Description = self.description
        levelmetadata.availBlue = self.availBlue
        levelmetadata.availGreen = self.availGreen
        levelmetadata.availYellow = self.availYellow
        levelmetadata.availRed = self.availRed
        return levelmetadata

    class Config:
        orm_mode = True


class LevelMetaDatasOut(Response):

    levels: List[LevelMetaDataOut]

    def to_proto(self):
        levelmetadatas = LevelMetaDataList_pb2.LevelMetaDataList()
        for x in self.levels:
            levelmetadatas.levels.append(x.to_proto())
        return levelmetadatas


    class Config:
        orm_mode = True


class LevelMetaDataRequest(Request):
    ulid: int

    class Config:
        orm_mode = True


class LevelMetaDataCreate(Request):
    name: str
    description: str

    class Config:
        orm_mode = True
