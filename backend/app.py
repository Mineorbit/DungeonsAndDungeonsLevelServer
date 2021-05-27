from fastapi import FastAPI

import config

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Dungeons And Dungeons LevelServer API v"+config.VERSION}


@app.get("/version")
async def root():
    return {"version": config.VERSION}


