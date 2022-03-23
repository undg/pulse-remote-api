import sys
from fastapi import FastAPI
from controllers.cors import setupCORS

from models.volume import ISink_serialize, IVolume_Info

from controllers.volume_app import (
    volume_app_info,
    volume_app_toggle,
    volume_app_down,
    volume_app_set,
    volume_app_up,
)

from controllers.volume_dev_out import (
    volume_dev_out_set,
    volume_dev_out_up,
    volume_dev_out_down,
    volume_dev_out_toggle,
    volume_dev_out_info,
)


sys.path.append(".")
app = FastAPI()
setupCORS(app)


# Out devices
@app.get("/volume-device-out/set/{vol}/{card}", response_model=list[ISink_serialize])
def vdo_set(vol: int, card: int):
    """
    Set volume in percent for output device with given index.
    """
    return volume_dev_out_set(vol, card)


@app.get("/volume-device-out/up/{card}", response_model=list[ISink_serialize])
def vdo_up(card: int):
    """
    Set volume up for output device with given index.
    """
    return volume_dev_out_up(card)


@app.get("/volume-device-out/down/{card}", response_model=list[ISink_serialize])
def vdo_down(card: int):
    """
    Set volume down for output device with given index.
    """
    return volume_dev_out_down(card)


@app.get("/volume-device-out/toggle/{card}", response_model=list[ISink_serialize])
def vdo_mute(card: int):
    """
    Toggle mute for output device with given index.
    """
    return volume_dev_out_toggle(card)


@app.get("/volume-device-out/info", response_model=list[ISink_serialize])
def vdo_info():
    """
    Get informations for output device with given index.
    """
    return volume_dev_out_info()


# Applications
@app.get("/volume-app/info", response_model=list[IVolume_Info])
def va_info():
    return volume_app_info()


@app.get("/volume-app/up/{index}", response_model=IVolume_Info)
def va_up(index: int):
    return volume_app_up(index)


@app.get("/volume-app/down/{index}", response_model=IVolume_Info)
def va_down(index: int):
    return volume_app_down(index)


@app.get("/volume-app/set/{vol}/{index}", response_model=IVolume_Info)
def va_set(index: int, vol: float):
    """
    Set volume in percent for application with given index.
    """
    return volume_app_set(index, vol)


@app.get("/volume-app/toggle/{index}", response_model=IVolume_Info)
def va_toggle(index: int):
    return volume_app_toggle(index)

# In devices
