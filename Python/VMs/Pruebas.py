#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'juan'
import commands,re,fnmatch
from EstadoVM import genera_estado_html,estado


name = "windows123456"
commands.getoutput("sed -i 's/\*/" + str(name) +"/g' /home/juan/Autounattend.xml")