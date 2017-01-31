#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_api
'''
:author:  madkote
:contact: madkote(at)bluewin.ch

Test
----
Unit tests for Flask app

Usage
-----
>>> python test_api.py
'''

import json
import unittest

import api
import settings

VERSION = (0, 1, 0)

__all__ = []
__author__ = 'madkote <madkote(at)bluewin.ch>'
__version__ = '.'.join(str(x) for x in VERSION)


# =============================================================================
# TESTS
# =============================================================================
class Test(unittest.TestCase):

    def setUp(self):
        api.app.config['TESTING'] = True
        self.client = api.app.test_client()

    def tearDown(self):
        api.app.config['TESTING'] = False

    def test_data(self):
        route = settings.API_URL + '/data'
        r = self.client.get(route)
        res = json.loads(r.data.decode())
        # these data may vary
        res.pop('version')
        res.pop('host')
        res.pop('node')
        res.pop('system')
        exp = {'data': 'some data'}
        self.assertTrue(res == exp,
                        'Route >%s should return %s, but got %s' %
                        (route, exp, res))

if __name__ == "__main__":
    unittest.main()
