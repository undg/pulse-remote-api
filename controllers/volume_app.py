from typing import Any
import pulsectl

def volume_app_info():
    p = pulsectl.Pulse("sinks")
    sinks = []
    for sink in p.sink_input_list():
        input_sink_serialized = {
            "index" : int(sink.index),
            "mute" : bool(sink.mute),
            "name" : str(sink.name),
            "volume": p.volume_get_all_chans(sink),
        }
        sinks.append(input_sink_serialized)

    p.close()
    return sinks

def volume_app_toggle(index):
    p = pulsectl.Pulse('volume-set')
    sink: Any = p.sink_input_info(index)

    mute = 0 if sink.mute == 1 else 1
    p.mute(sink, mute)

    input_sink_serialized = {
        "index" : sink.index,
        "mute" : sink.mute,
        "name" : sink.name,
        "volume": p.volume_get_all_chans(sink),
    }

    p.close()
    return input_sink_serialized

def volume_app_set(index: int, vol: float):
    p = pulsectl.Pulse('volume-set')
    sink: Any = p.sink_input_info(index)

    p.volume_set_all_chans(sink, vol / 100)

    input_sink_serialized = {
        "index" : sink.index,
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
        "index" : sink.index,
        "mute" : sink.mute,
        "name" : sink.name,
        "volume": p.volume_get_all_chans(sink),
    }

    p.close()
    return input_sink_serialized

def volume_app_up(index):
    return sink_input_volume(index, 0.05)

def volume_app_down(index):
    return sink_input_volume(index, -0.05)
