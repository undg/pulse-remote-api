from controllers.volume.common import Change, volume

def volume_down():
    return volume(Change.DOWN)
