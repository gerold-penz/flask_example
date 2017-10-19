#!/usr/bin/env python
# coding: utf-8
"""
Installiert oder updated die Python-Requirements
"""

import os
import subprocess

THISDIR = os.path.dirname(os.path.abspath(__file__))
BASEDIR = os.path.abspath(os.path.join(THISDIR, ".."))
APPDIR = os.path.join(BASEDIR, "application")
LIBDIR = os.path.join(APPDIR, "lib")


def main():
    
    os.chdir(APPDIR)
    print u"Install requirements..."

    # Argumente zusammensetzen
    args = [
        "pip",
        "install",
        "-t", LIBDIR,
        "--upgrade",
        "-r", "requirements.txt"
    ]

    # Hochladen
    returncode = subprocess.call(args = args, cwd = APPDIR)
    if returncode != 0:
        raw_input("Press ENTER to continue...")


if __name__ == "__main__":
    main()


