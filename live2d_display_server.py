import json
import os

from flask import Flask, send_from_directory


app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    root_dir = os.path.dirname(os.path.abspath(__file__))

    return send_from_directory(root_dir, 'index.html')


@app.route('/assets/<path:path>')
def serve_static(path):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir,"assets"), path)

@app.route('/src/<path:path>')
def serve_src(path):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir,"src"), path)

@app.route('/api/get_mouth_y')
def api_get_one_account():

    with open("tmp.txt", "r") as f:
        return json.dumps({
            "y": f.read()
        })


if __name__ == '__main__':
    app.run(port=4800, debug=True, host="0.0.0.0")