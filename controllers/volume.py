import pulsectl
from models.sink import sink_serialize
from enum import Enum


class Value(Enum):
    UP = "up"
    DOWN = "down"
    TOGGLE = "toggle"
    INFO = "info"
    SET = "set"


def volume(change: Value, vol: int = 0):

    sinks = []

    pulse = pulsectl.Pulse("volume-changer")
    for sink in pulse.sink_list():
        # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
        if change == Value.UP:
            pulse.volume_change_all_chans(sink, 0.05)
        elif change == Value.DOWN:
            pulse.volume_change_all_chans(sink, -0.05)
        elif change == Value.INFO:
            pulse.volume_get_all_chans(sink)
        elif change == Value.SET:
            pulse.volume_set_all_chans(sink, vol / 100)
        elif change == Value.TOGGLE:
            if sink.mute == 1:
                pulse.mute(sink, 0)
            else:
                pulse.mute(sink, 1)
        sinks.append(sink_serialize(sink))

    return sinks

def volume_down():
    return volume(Value.DOWN)

def volume_up():
    return volume(Value.UP)

def volume_toggle():
    return volume(Value.TOGGLE)

def volume_info():
    return volume(Value.INFO)

def volume_set(vol: int):
    return volume(Value.SET, vol)
