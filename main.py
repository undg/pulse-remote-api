import sys
from fastapi import FastAPI
from controllers.volume import volume_set, volume_up, volume_down, volume_toggle, volume_info
from controllers.cors import setupCORS

sys.path.append(".")
app = FastAPI()
setupCORS(app)

@app.get("/volume/set/{vol}")
def vol_set(vol: str):
    return volume_set(int(vol))

@app.get("/volume/up")
def vol_up():
    return volume_up()

@app.get("/volume/down")
def vol_down():
    return volume_down()


@app.get("/volume/toggle")
def vol_mute():
    return volume_toggle()


@app.get("/volume/info")
def vol_info():
    return volume_info()

