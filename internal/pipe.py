from pyuv import Loop
from pyuv import Pipe

BOUNDARY = "--BAS-BOUNDARY--"


class PythonPipe:

    def __init__(self):
        self.__loop = Loop.default_loop()
        self.__pipe = Pipe(self.__loop)
        self.__on_data = None
        self.__all_data = ''

    def __on_connect(self, pipe, err):
        self.__pipe.start_read(self.__on_read)

    def __on_read(self, pipe, data, err):
        self.__all_data += str(data, 'utf-8')
        chunk = self.__all_data.split(BOUNDARY)

        if len(chunk[-1]) != 0:
            self.__all_data = chunk[-1]
        else:
            self.__all_data = ''

        chunk.pop()

        for val in chunk:
            self.__on_data(val)

    def init(self, pid, on_data):
        self.__pipe.connect(r'\\?\pipe\basembeddedpipespython3.7.4' + str(pid), self.__on_connect)
        self.__on_data = on_data
        self.__loop.run()

    def write(self, text):
        self.__pipe.write(str.encode(text + BOUNDARY))
