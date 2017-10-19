#!/usr/bin/env python
# coding: utf-8

import os
import subprocess


THISDIR = os.path.dirname(os.path.abspath(__file__))
BASEDIR = os.path.abspath(os.path.join(THISDIR, ".."))
APPDIR = os.path.join(BASEDIR, "application")
FLASK = "/usr/local/bin/flask"
FLASK_APP = os.path.join(APPDIR, "anwendung.py")


if __name__ == "__main__":

    args = [
        FLASK,
        "run",
        "--host", "0.0.0.0",
        "--port", "5000",
        "--reload",
        "--debugger",
    ]
    env = {"FLASK_APP": FLASK_APP}

    print u"Serving HTTP on port 5000..."
    subprocess.call(args, env = env, cwd = APPDIR)
