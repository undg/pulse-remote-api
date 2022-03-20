from typing import Any
import pulsectl

def sink_input_info():
    p = pulsectl.Pulse("sinks")
    sinks = []
    for sink in p.sink_input_list():
        input_sink_serialized = {
            "id" : int(sink.index),
            "mute" : bool(sink.mute),
            "name" : str(sink.name),
            "volume": p.volume_get_all_chans(sink),
        }
        sinks.append(input_sink_serialized)

    p.close()
    return sinks

def sink_input_volume_set(index: int, vol: float):
    p = pulsectl.Pulse('volume-set')
    sink: Any = p.sink_input_info(index)

    p.volume_set_all_chans(sink, vol / 100)

    input_sink_serialized = {
        "id" : sink.index,
        "mute" : sink.mute,
        "name" : sink.name,
        "volume": p.volume_get_all_chans(sink),
    }

    p.close()
    return input_sink_serialized

def sink_input_volume(index: int, inc: float):
    p = pulsectl.Pulse("sink-input-volume-change")
    # There is strange pyrigh error. Any is not so elegant, but it's muting it.
    sink: Any = p.sink_input_info(index)

    p.volume_change_all_chans(sink, inc)

    input_sink_serialized = {
        "id" : sink.index,
        "mute" : sink.mute,
        "name" : sink.name,
        "volume": p.volume_get_all_chans(sink),
    }

    p.close()
    return input_sink_serialized

def sink_input_volume_up(index):
    return sink_input_volume(index, 0.05)

def sink_input_volume_down(index):
    return sink_input_volume(index, -0.05)
