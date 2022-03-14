import pulsectl

def sink_input_list():
    pulse = pulsectl.Pulse("sinks")
    sinks = []
    for sink in pulse.sink_input_list():
        print(sink)
        input_sink_serialized = {
            "id" : int(sink.index),
            "mute" : bool(sink.mute),
            "name" : str(sink.name),
        }
        sinks.append(input_sink_serialized)

    pulse.close()
    return sinks
