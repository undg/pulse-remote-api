from flask import jsonify

def index():
    return jsonify({"code": "1", "message": "Sunshines and roses."})

