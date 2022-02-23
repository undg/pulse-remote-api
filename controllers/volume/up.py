from controllers.volume.common import Change, volume

def volume_up():
    return volume(Change.UP)
