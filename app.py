#!/usr/bin/env python

import json
import db
import logging

from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# Load config file
config = json.loads(open('config.json', 'r').read())

# TODO(naum): use config.json to properly configure logger
# Setup logging
log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# Setup database
db.apply_migrations()


# Run dev application
if __name__ == '__main__':
    app.run(debug = config['dev']['debug'], extra_files = ['config.json'])
