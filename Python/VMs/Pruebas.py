#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'juan'
import commands,re,fnmatch
from EstadoVM import genera_estado_html,estado
valor=0


try:
    valor = int(valor)
    print "todo ok"
except ValueError:
    print("Oops!  That was no valid number.  Try again...")