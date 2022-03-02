#!/bin/python
import sys
from flask_apispec.annotations import doc

from marshmallow.schema import Schema
sys.path.append('.')

from flask import Flask
app = Flask(__name__)

from controllers.volume import volume_up, volume_down, volume_toggle, volume_info

from flask_apispec import marshal_with, use_kwargs

class VolumeStatusSchema(Schema):
    class Meta:
        fields = ('volume', 'name', 'value', 'description')


@app.route("/volume/up")
@use_kwargs({})
@marshal_with(VolumeStatusSchema)
@doc(description='Audio device (general volume) controller. Volume info in response.')
def vol_up():
    return volume_up()

@app.route("/volume/down")
@use_kwargs({})
@marshal_with(VolumeStatusSchema)
@doc(description='Audio device (general volume) controller. Volume info in response.')
def vol_down():
    return volume_down()

@app.route("/volume/mute")
@use_kwargs({})
@marshal_with(VolumeStatusSchema)
@doc(description='Audio device (general volume) controller. Volume info in response.')
def vol_mute():
    return volume_toggle()

@app.route("/volume/info")
@use_kwargs({})
@marshal_with(VolumeStatusSchema)
@doc(description='Audio device (general volume) controller. Volume info in response.')
def vol_info():
    return volume_info()

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)
