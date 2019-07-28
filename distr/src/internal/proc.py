import threading
import signal
import sys
import os

class PythonProc:

    def _init_(self):
        self.pid = sys.argv[2]

    def init(self):
        def func():
           self.init(self.pid)
           try:
              os.kill(self.pid, 0)
           except:
              sys.exit()
        threading.Timer(1, func).start()
