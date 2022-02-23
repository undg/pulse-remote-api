def sink_serialize(sink):
    # I'm not sure if this is true. Speakers are elements of list, I'm not sure what are order rules. I have stereo and HDMI 5.1 so those two should be OK. Rest is just guessing.
    volume = []
    if len(sink.volume.values) == 1:
        volume = [{'name': "Mono", 'value': sink.volume.values[0]}]
    elif len(sink.volume.values) == 2:
        volume = [
            {'name': "Front Left", 'value': sink.volume.values[0]},
            {'name': "Front Right", 'value': sink.volume.values[1]},
        ]
    elif len(sink.volume.values) == 3:
        volume = [
            {'name': "Front Left", 'value': sink.volume.values[0]},
            {'name': "Front Right", 'value': sink.volume.values[1]},
            {'name': "Subwoofer", 'value': sink.volume.values[2]},
        ]
    elif len(sink.volume.values) == 4:
        volume = [
            {'name': "Front Left", 'value': sink.volume.values[0]},
            {'name': "Front Right", 'value': sink.volume.values[1]},
            {'name': "Rear Left", 'value': sink.volume.values[2]},
            {'name': "Rear Right", 'value': sink.volume.values[3]},
        ]
    elif len(sink.volume.values) == 5:
        volume = [
            {'name': "Front Left", 'value': sink.volume.values[0]},
            {'name': "Front Right", 'value': sink.volume.values[1]},
            {'name': "Rear Left", 'value': sink.volume.values[2]},
            {'name': "Rear Right", 'value': sink.volume.values[3]},
            {'name': "Subwoofer", 'value': sink.volume.values[4]},
        ]
    elif len(sink.volume.values) == 6:
        volume = [
            {'name': "Front Left", 'value': sink.volume.values[0]},
            {'name': "Front Right", 'value': sink.volume.values[1]},
            {'name': "Rear Left", 'value': sink.volume.values[2]},
            {'name': "Rear Right", 'value': sink.volume.values[3]},
            {'name': "Front Center", 'value': sink.volume.values[4]},
            {'name': "Subwoofer", 'value': sink.volume.values[5]},
        ]
    else:
        volume = {"unknown": sink.volume.values[0]}

    return {
        "volume": volume,
        "description": sink.description,
        "name": sink.name,
        "index": sink.index,
        "mute": sink.mute,
        "raw": str(sink)
    }

