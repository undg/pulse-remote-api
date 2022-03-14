import sys
from fastapi import FastAPI
from controllers.sinks import sink_input_list
from controllers.volume import volume_set, volume_up, volume_down, volume_toggle, volume_info
from controllers.cors import setupCORS
from pydantic import BaseModel

from models.sink import Sink_serialize_model

sys.path.append(".")
app = FastAPI()
setupCORS(app)

@app.get("/volume/set/{vol}", response_model=list[Sink_serialize_model])
def v_set(vol: int):
    return volume_set(vol)

@app.get("/volume/up", response_model=list[Sink_serialize_model])
def v_up():
    return volume_up()

@app.get("/volume/down", response_model=list[Sink_serialize_model])
def v_down():
    return volume_down()


@app.get("/volume/toggle", response_model=list[Sink_serialize_model])
def v_mute():
    return volume_toggle()


@app.get("/volume/info", response_model=list[Sink_serialize_model])
def v_info():
    return volume_info()

class Sink_input_list_model(BaseModel):
    id: int
    mute: bool
    name: str

@app.get("/sink/input/list", response_model=list[Sink_input_list_model])
def s_input_list():
    return sink_input_list()

