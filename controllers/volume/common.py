import pulsectl
from models.sink import sink_serialize
from flask import jsonify
from enum import Enum


class Change(Enum):
    UP = "UP"
    DOWN = "DOWN"
    MUTE = "MUTE"


def volume(change: Change):

    sinks = []

    pulse = pulsectl.Pulse("volume-changer")
    for sink in pulse.sink_list():
        # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
        if change == Change.UP:
            pulse.volume_change_all_chans(sink, 0.1)
        elif change == Change.DOWN:
            pulse.volume_change_all_chans(sink, -0.1)
        elif change == Change.MUTE:
            if sink.mute == 1:
                pulse.mute(sink, 0)
            else:
                pulse.mute(sink, 1)
        sinks.append(sink_serialize(sink))

    return jsonify(sinks)
