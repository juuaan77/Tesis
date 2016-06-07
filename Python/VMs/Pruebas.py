#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'juan'

import threading,commands
mutex = threading.Lock()
def worker(num):
    """thread worker function"""

    mutex.acquire()
    commands.getoutput("echo 'Worker: %s' >> /home/juan/hilos" % num)
    mutex.release()
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()