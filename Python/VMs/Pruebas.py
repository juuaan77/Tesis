#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'juan'

import commands
import sys

ram = 512
disco = 10

try:
    if int(ram)<1024:
        print "exito"
except ValueError:
    print "error"

print type(ram)