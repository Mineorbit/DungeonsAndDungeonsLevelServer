from fastapi import APIRouter

import config

router = APIRouter()


@router.get("/", tags=["base"])
async def root():
    return {"message": "Welcome to the Dungeons And Dungeons LevelServer API v" + config.VERSION}


@router.get("/version", tags=["base"])
async def get_version():
    return {"version": config.VERSION}