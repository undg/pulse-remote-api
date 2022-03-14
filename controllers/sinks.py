import pulsectl



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
