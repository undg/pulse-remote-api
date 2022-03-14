import sys
from fastapi import FastAPI
from controllers.sinks import sink_input_list
from controllers.volume import volume_set, volume_up, volume_down, volume_toggle, volume_info
from controllers.cors import setupCORS

sys.path.append(".")
app = FastAPI()
setupCORS(app)

@app.get("/volume/set/{vol}")
def v_set(vol: str):
    return volume_set(int(vol))

@app.get("/volume/up")
def v_up():
    return volume_up()

@app.get("/volume/down")
def v_down():
    return volume_down()


@app.get("/volume/toggle")
def v_mute():
    return volume_toggle()


@app.get("/volume/info")
def v_info():
    return volume_info()

@app.get("/sink/input/list")
def s_input_list():
    return sink_input_list()

