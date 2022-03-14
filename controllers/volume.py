import pulsectl
from models.sink import sink_serialize
from enum import Enum


class Value(Enum):
    UP = "up"
    DOWN = "down"
    TOGGLE = "toggle"
    INFO = "info"
    SET = "set"


def volume(change: Value, vol: int = 0):

    sinks = []

    pulse = pulsectl.Pulse("volume-changer")
    for audio_card in pulse.sink_list():
        # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
        if change == Value.UP:
            pulse.volume_change_all_chans(audio_card, 0.05)
        elif change == Value.DOWN:
            pulse.volume_change_all_chans(audio_card, -0.05)
        elif change == Value.INFO:
            pulse.volume_get_all_chans(audio_card)
        elif change == Value.SET:
            pulse.volume_set_all_chans(audio_card, vol / 100)
        elif change == Value.TOGGLE:
            mute = 0 if audio_card.mute == 1 else 1
            pulse.mute(audio_card, mute)
        sinks.append(sink_serialize(audio_card))

    pulse.close()

    return sinks


def volume_down():
    return volume(Value.DOWN)


def volume_up():
    return volume(Value.UP)


def volume_toggle():
    return volume(Value.TOGGLE)


def volume_info():
    return volume(Value.INFO)


def volume_set(vol: int):
    return volume(Value.SET, vol)
