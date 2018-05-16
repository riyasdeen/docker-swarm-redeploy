"""
This script runs the docker_swarm_redeploy application using a development server.
"""

from os import environ

from flask import Flask
from flask import request
from flask import jsonify
import json
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify(response='ok'), 200

@app.route('/', methods=['POST'])
def hook_listen():
    if request.method == 'POST':
        token = request.args.get('token')
        if token == environ.get("TOKEN"):
            post_data = request.get_json(silent=True)
            subprocess.Popen("/bin/sh /redeploy " + "{}:{}".format(post_data['repository']['repo_name'], post_data['push_data']['tag']), shell=True)
            return jsonify(success=True), 200
        else:
            return jsonify(success=False, error="Invalid token"), 400

if __name__ == '__main__':
    print(environ.get('TOKEN', 'sdadads'))
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
