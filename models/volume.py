from pydantic.main import BaseModel


class IVolume_Info(BaseModel):
    index: int
    mute: bool
    name: str
    volume: float


class IVolume(BaseModel):
    name: str
    value: float


class ISink_serialize(BaseModel):
    volume: list[IVolume]
    description: str
    name: str
    index: int
    mute: bool
    raw: str


def sink_serialize(sink):
    # I'm not sure if this is true. Speakers are elements of list, I'm not sure what are order rules. I have stereo and 5.1 so those two should be OK. Rest is just guessing.
    channels = [{"name": "Unknown as mono", "value": sink.volume.values[0]}]
    if len(sink.volume.values) == 1:
        channels = [{"name": "Mono", "value": sink.volume.values[0]}]
    if len(sink.volume.values) == 2:
        channels = [
            {"name": "Front Left", "value": sink.volume.values[0]},
            {"name": "Front Right", "value": sink.volume.values[1]},
        ]
    elif len(sink.volume.values) == 3:
        channels = [
            {"name": "Front Left", "value": sink.volume.values[0]},
            {"name": "Front Right", "value": sink.volume.values[1]},
            {"name": "Subwoofer", "value": sink.volume.values[2]},
        ]
    elif len(sink.volume.values) == 4:
        channels = [
            {"name": "Front Left", "value": sink.volume.values[0]},
            {"name": "Front Right", "value": sink.volume.values[1]},
            {"name": "Rear Left", "value": sink.volume.values[2]},
            {"name": "Rear Right", "value": sink.volume.values[3]},
        ]
    elif len(sink.volume.values) == 5:
        channels = [
            {"name": "Front Left", "value": sink.volume.values[0]},
            {"name": "Front Right", "value": sink.volume.values[1]},
            {"name": "Rear Left", "value": sink.volume.values[2]},
            {"name": "Rear Right", "value": sink.volume.values[3]},
            {"name": "Subwoofer", "value": sink.volume.values[4]},
        ]
    elif len(sink.volume.values) == 6:
        channels = [
            {"name": "Front Left", "value": sink.volume.values[0]},
            {"name": "Front Right", "value": sink.volume.values[1]},
            {"name": "Rear Left", "value": sink.volume.values[2]},
            {"name": "Rear Right", "value": sink.volume.values[3]},
            {"name": "Front Center", "value": sink.volume.values[4]},
            {"name": "Subwoofer", "value": sink.volume.values[5]},
        ]

    return {
        "volume": channels,
        "description": sink.description,
        "name": sink.name,
        "index": sink.index,
        "mute": sink.mute,
        "raw": str(sink),
    }
