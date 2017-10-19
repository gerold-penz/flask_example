#!/usr/bin/env python
# coding: utf-8

import flask
import textwrap
from . import testpage

blueprint = flask.Blueprint("", __name__)


@blueprint.route("/")
def index():

    return textwrap.dedent(u"""
    <html>
    <body>
      <h1>Servus Österreich</h1>
      <p>
        <a href="/testpage/">Zur Testseite</a>
      </p>
    </body>
    </html>
    """)

