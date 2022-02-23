#!/bin/python
import sys
sys.path.append('.')

from flask import Flask

from controllers.index import index
from routes.volume_bp import volume_bp

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    res = index()
    return res

app.register_blueprint(volume_bp, url_prefix='/volume')

if __name__ == "__main__":
    app.debug = True
    app.env = "development"
    app.run()
