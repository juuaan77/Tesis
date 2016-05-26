#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'juan'
import commands,re,fnmatch
from EstadoVM import genera_estado_html,estado

salida = commands.getstatusoutput("whoami")
print salida

commands.getstatusoutput("echo " +salida[1] + " >> /home/juan/cron")
