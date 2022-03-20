import sys
from fastapi import FastAPI
from controllers.cors import setupCORS

from controllers.sinks import (
    sink_input_info,
    sink_input_volume_down,
    sink_input_volume_set,
    sink_input_volume_up,
)
from models.sink import ISink_serialize, ISink_input
from controllers.volume import (
    volume_set,
    volume_up,
    volume_down,
    volume_toggle,
    volume_info,
)


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
def v_mute(card: int):
    return volume_toggle(card)


@app.get("/volume/info", response_model=list[ISink_serialize])
def v_info():
    return volume_info()


@app.get("/sink/input/info", response_model=list[ISink_input])
def s_input_info():
    return sink_input_info()


@app.get("/sink/input/up/{index}", response_model=ISink_input)
def s_input_volume_up(index: int):
    return sink_input_volume_up(index)


@app.get("/sink/input/down/{index}", response_model=ISink_input)
def s_input_volume_down(index: int):
    return sink_input_volume_down(index)


@app.get("/sink/input/set/{vol}/{index}", response_model=ISink_input)
def s_input_volume_set(index: int, vol: float):
    return sink_input_volume_set(index, vol)
