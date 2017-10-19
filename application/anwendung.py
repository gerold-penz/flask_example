#!/usr/bin/env python
# coding: utf-8

import os
import sys

LIBDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
sys.path.insert(1, LIBDIR)

import flask
import http_root


# WSGI-App
app = flask.Flask(__name__)


# Einstellungen
app.config.update({
    "DEBUG": True,
    "TESTING": True,
})


# Seiten registrieren
app.register_blueprint(http_root.blueprint)
app.register_blueprint(http_root.testpage.blueprint)
