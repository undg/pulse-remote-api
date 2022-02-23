from flask import Blueprint, jsonify

from controllers.volume.up import volume_up
from controllers.volume.down import volume_down
from controllers.volume.mute import volume_mute


volume_bp = Blueprint("volume_bp", __name__)

volume_bp.route("/up", methods=["GET"])(volume_up)
volume_bp.route("/down", methods=["GET"])(volume_down)
volume_bp.route("/mute", methods=["GET"])(volume_mute)

