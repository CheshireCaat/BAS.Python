from pyuv import Loop
from pyuv import Pipe
import sys

BOUNDARY = '--BAS-BOUNDARY--'

#  \\.\pipe\basembeddedpipespython3.7.38038
class PythonPipe:

    def __init__(self):
        self.__pipe = Pipe(Loop.default_loop())
        self.__callback = None
        self.__buffer = ''

    def __on_connect(self, pipe, err):
        self.__pipe.start_read(self.__on_read)

    def __on_read(self, pipe, data, err):
        self.__buffer += data.decode('utf-8')
        chunk = self.__buffer.split(BOUNDARY)

        if len(chunk[-1]) != 0:
            self.__buffer = chunk.pop()
        else:
            self.__buffer = ''

        for val in chunk: self.__callback(val)

    def init(self, callback):
        self.__pipe.connect(r'\\?\pipe\basembeddedpipespython3.7.3' + sys.argv[2], self.__on_connect)
        self.__callback = callback
        self.__pipe.loop.run()

    def write(self, text):
        self.__pipe.write(str.encode(text + BOUNDARY))
