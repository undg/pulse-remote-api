import json
import pulsectl
from models.sink import sink_serialize

from utils.MyEncoder import MyEncoder


def sink_input_list():
    pulse = pulsectl.Pulse("sinks")
    sinks = []
    for sink in pulse.sink_input_list():
        print(sink)
        s = {
            "id" : sink.index,
            "mute" : sink.mute,
            "name" : sink.name,
        }
        sinks.append(s)

    pulse.close()
    return sinks
