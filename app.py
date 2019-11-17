#!/usr/bin/env python

import json
from flask import Flask
app = Flask(__name__, static_folder='static')


@app.route('/')
def hello_world():
    return 'Hello, World!'

config = json.loads(open('config.json', 'r').read())

if __name__ == '__main__':
    config = config['debug']
    app.run(host  = config['host'],
            port  = config['port'],
            debug = config['debug'],
            extra_files = ['config.json'])
