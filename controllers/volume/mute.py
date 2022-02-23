from controllers.volume.common import Change, volume

def volume_mute():
    return volume(Change.MUTE)
