#!/bin/python
import sys
sys.path.append('.')

from fastapi import FastAPI
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
def setupCORS(app):
    port = "3000"
    origins = [
        "http://192.168.1.222:" + port,
        "https://192.168.1.222:" + port,
        "http://cm:" + port,
        "https://cm:" + port,
        "http://127.0.0.1:" + port,
        "https://127.0.0.1:" + port,
        "http://localhost:" + port,
        "https://loacalhost:" + port,
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

setupCORS(app)

from controllers.volume import volume_up, volume_down, volume_toggle, volume_info

@app.get("/volume/up")
def vol_up():
    return volume_up()

@app.get("/volume/down")
def vol_down():
    return volume_down()

@app.get("/volume/mute")
def vol_mute():
    return volume_toggle()

@app.get("/volume/info")
def vol_info():
    return volume_info()

