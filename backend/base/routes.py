from fastapi import APIRouter

import config

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the Dungeons And Dungeons LevelServer API v"+config.VERSION}


@router.get("/version")
async def root():
    return {"version": config.VERSION}