import pulsectl
from models.sink import sink_serialize
from enum import Enum


class Value(Enum):
    UP = "up"
    DOWN = "down"
    TOGGLE = "toggle"
    INFO = "info"
    SET = "set"


def volume(change: Value, vol: int = 0, card: int = None):

    pulse = pulsectl.Pulse("volume-changer")

    for audio_card in pulse.sink_list():
        if card == audio_card.index:
            volume = audio_card.volume
            if change == Value.UP:
                volume.value_flat += 0.05
            elif change == Value.DOWN:
                volume.value_flat -= 0.05
            elif change == Value.SET:
                volume.value_flat = vol / 100
            elif change == Value.TOGGLE:
                mute = 0 if audio_card.mute == 1 else 1
                pulse.mute(audio_card, mute)
            elif change == Value.INFO:
                pulse.volume_get_all_chans(audio_card)

            pulse.volume_set(audio_card, volume)

    sinks = []
    for audio_card in pulse.sink_list():
        sinks.append(sink_serialize(audio_card))
    pulse.close()

    return sinks


def volume_dev_out_down(card: int = None):
    return volume(Value.DOWN, 0, card)


def volume_dev_out_up(card: int = None):
    return volume(Value.UP, 0, card)


def volume_dev_out_toggle(card: int = None):
    return volume(Value.TOGGLE, 0, card)


def volume_dev_out_info():
    return volume(Value.INFO)


def volume_dev_out_set(vol: int, card: int):
    return volume(Value.SET, vol, card)
