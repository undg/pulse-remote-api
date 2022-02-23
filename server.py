#!/bin/python
from flask import Flask, jsonify
import json
import pulsectl


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"code": "1", "message": "Sunshines and roses."})

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


@app.route("/volume/up", methods=["GET"])
def volume_up():
    with pulsectl.Pulse("volume-increaser") as pulse:
        sinks = []
        for sink in pulse.sink_list():
            # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
            pulse.volume_change_all_chans(sink, 0.1)
            sinks.append(sink_serialize(sink))
        return jsonify(sinks)


@app.route("/volume/down", methods=["GET"])
def volume_down():
    with pulsectl.Pulse("volume-decreaser") as pulse:
        sinks = []
        for sink in pulse.sink_list():
            # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
            pulse.volume_change_all_chans(sink, -0.1)
            sinks.append(sink_serialize(sink))
        return jsonify(sinks)


if __name__ == "__main__":
    app.run()
