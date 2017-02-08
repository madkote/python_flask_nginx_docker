#!/usr/bin/env python
# -*- coding: utf-8 -*-
# settings
'''
:author:  madkote
:contact: madkote(at)bluewin.ch

Settings
--------
Settings for Flask app

:note: host can not be 'localhost' since it must be accessable outside of
       the docker image.
'''

# import socket
import uuid

VERSION = (0, 1, 0)

__all__ = []
__author__ = 'madkote <madkote(at)bluewin.ch>'
__version__ = '.'.join(str(x) for x in VERSION)

API_FLAG_DEBUG = False
API_FLAG_THREADED = True
# API_HOST = socket.gethostbyname(socket.gethostname())
# API_HOST = '127.0.0.1'
API_HOST = '0.0.0.0'
API_PORT = 5000
API_NAME = 'flask_nginx_docker'
API_SECRET_KEY = str(uuid.uuid4())
API_VERSION = '1.0'
API_URL = '/api/v%s' % API_VERSION
