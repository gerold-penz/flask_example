#!/usr/bin/env python
# coding: utf-8

import os
import sys

THISDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, THISDIR)

from anwendung import app as application

