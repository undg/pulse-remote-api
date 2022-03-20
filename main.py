import sys
from fastapi import FastAPI
from fastapi.params import Path
from controllers.cors import setupCORS

from controllers.sinks import (
    sink_input_info,
    sink_input_toggle,
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


# Out devices
@app.get("/volume-device-out/set/{vol}/{card}", response_model=list[ISink_serialize])
def v_set(vol: int, card: int):
    """
    Set volume in percent for output device with given index.
    """
    return volume_set(vol, card)


@app.get("/volume-device-out/up/{card}", response_model=list[ISink_serialize])
def v_up(card: int):
    """
    Set volume up for output device with given index.
    """
    return volume_up(card)


@app.get("/volume-device-out/down/{card}", response_model=list[ISink_serialize])
def v_down(card: int):
    """
    Set volume down for output device with given index.
    """
    return volume_down(card)


@app.get("/volume-device-out/toggle/{card}", response_model=list[ISink_serialize])
def v_mute(card: int):
    """
    Toggle mute for output device with given index.
    """
    return volume_toggle(card)


@app.get("/volume-device-out/info", response_model=list[ISink_serialize])
def v_info():
    """
    Get informations for output device with given index.
    """
    return volume_info()


# Applications
@app.get("/volume-app/info", response_model=list[ISink_input])
def s_input_info():
    return sink_input_info()


@app.get("/volume-app/up/{index}", response_model=ISink_input)
def s_input_volume_up(index: int):
    return sink_input_volume_up(index)


@app.get("/volume-app/down/{index}", response_model=ISink_input)
def s_input_volume_down(index: int):
    return sink_input_volume_down(index)


@app.get("/volume-app/set/{vol}/{index}", response_model=ISink_input)
def s_input_volume_set(index: int, vol: float):
    """
    Set volume in percent for application with given index.
    """
    return sink_input_volume_set(index, vol)


@app.get("/volume-app/toggle/{index}", response_model=ISink_input)
def s_input_toggle(index: int):
    return sink_input_toggle(index)

# In devices
