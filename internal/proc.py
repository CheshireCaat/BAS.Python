import threading
import sys
import os

class PythonProc:

    def init(self, pid):
        def func():
           try:
              os.kill(pid, 0)
           except:
              sys.exit(0)
           start(pid)
        t = threading.Timer(1, func)
        t.start()

    def __init__(self):
        pass
