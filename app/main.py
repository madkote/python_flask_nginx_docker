#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main
'''
:author:  madkote
:contact: madkote(at)bluewin.ch

Main
----
The main entry point

Usage
-----
>>> python main.py
'''

import api as app

VERSION = (0, 1, 0)

__all__ = []
__author__ = 'madkote <madkote(at)bluewin.ch>'
__version__ = '.'.join(str(x) for x in VERSION)


if __name__ == '__main__':
    app.run()
