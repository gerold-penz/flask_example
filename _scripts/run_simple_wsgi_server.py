#!/usr/bin/env python
# coding: utf-8

import os
import sys

THISDIR = os.path.dirname(os.path.abspath(__file__))
BASEDIR = os.path.abspath(os.path.join(THISDIR, ".."))
APPDIR = os.path.join(BASEDIR, "application")
sys.path.insert(1, APPDIR)

from wsgi_anwendung import app
from wsgiref.simple_server import make_server


if __name__ == "__main__":
    httpd = make_server("0.0.0.0", 5000, app)
    print u"Serving HTTP on port 5000..."
    httpd.serve_forever()

