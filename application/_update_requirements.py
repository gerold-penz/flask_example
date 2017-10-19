#!/usr/bin/env python
# coding: utf-8
"""
Installiert oder aktualisiert die Python-Requirements
"""

import os
import subprocess

THISDIR = os.path.dirname(os.path.abspath(__file__))
LIBDIR = os.path.join(THISDIR, "lib")


def main():
    
    os.chdir(THISDIR)
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
    returncode = subprocess.call(args = args, cwd = THISDIR)
    if returncode != 0:
        raw_input("Press ENTER to continue...")


if __name__ == "__main__":
    main()

