#!/usr/bin/env python
# -*- coding: utf-8 -*-
# api
'''
:author:  madkote
:contact: madkote(at)bluewin.ch

API
---
The Flask app as web API
'''

import platform
import socket

from flask import Flask
from flask import jsonify

import settings

VERSION = (0, 1, 0)

__all__ = ['run']
__author__ = 'madkote <madkote(at)bluewin.ch>'
__version__ = '.'.join(str(x) for x in VERSION)


# =============================================================================
# INITIALIZATION
# =============================================================================
app = Flask(settings.API_NAME)
app.config['SECRET_KEY'] = settings.API_SECRET_KEY


# =============================================================================
# API ROUTES
# =============================================================================
@app.route('/')
def index():
    return "Flask app %s is up and running at version %s" % (settings.API_NAME,
                                                             __version__)


@app.route(settings.API_URL + '/data', methods=['GET'])
def data():
    return jsonify({'data': 'some data',
                    'version': __version__,
                    'node': str(platform.node()),
                    'host': str(socket.gethostname()),
                    'system': platform.system()})


# =============================================================================
# RUNNER
# =============================================================================
def run():
    app.run(settings.API_HOST,
            settings.API_PORT,
            settings.API_FLAG_DEBUG,
            threaded=settings.API_FLAG_THREADED)
