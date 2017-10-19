#!/usr/bin/env python
# coding: utf-8

import flask

blueprint = flask.Blueprint("testpage", __name__)


@blueprint.route("/testpage/")
def index():

    # Fertig
    return u"Ich bin die Testseite /testpage/."
