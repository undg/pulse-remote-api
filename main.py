import sys
from fastapi import FastAPI
from controllers.cors import setupCORS

from controllers.sinks import sink_input_list
from models.sink import ISink_serialize, ISink_input_list
from controllers.volume import volume_set, volume_up, volume_down, volume_toggle, volume_info


sys.path.append(".")
app = FastAPI()
setupCORS(app)

@app.get("/volume/set/{vol}/{card}", response_model=list[ISink_serialize])
def v_set(vol: int, card: int):
    return volume_set(vol, card)

@app.get("/volume/up/{card}", response_model=list[ISink_serialize])
def v_up(card: int):
    return volume_up(card)

@app.get("/volume/down/{card}", response_model=list[ISink_serialize])
def v_down(card: int):
    return volume_down(card)


@app.get("/volume/toggle/{card}", response_model=list[ISink_serialize])
def v_mute(card: int ):
    return volume_toggle(card)


@app.get("/volume/info", response_model=list[ISink_serialize])
def v_info():
    return volume_info()


@app.get("/sink/input/list", response_model=list[ISink_input_list])
def s_input_list():
    return sink_input_list()

