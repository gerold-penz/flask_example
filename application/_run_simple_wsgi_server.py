#!/usr/bin/env python
# coding: utf-8

import os
from anwendung import app
from wsgiref.simple_server import make_server

THISDIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    os.chdir(THISDIR)
    httpd = make_server("0.0.0.0", 5000, app)
    print u"Serving HTTP on port 5000..."
    httpd.serve_forever()

