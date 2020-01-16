import json
import os

from pyuv import Loop, Pipe

from .constants import NEED_STOP, BOUNDARY


def check_process(data: object) -> None:
    if data is None:
        os.kill(os.getpid(), 2)


class Pipes:
    handler = None
    buffer = ''

    def __init__(self):
        self.pipe = Pipe(Loop.default_loop())

    def run(self, handler, pid):
        self.handler = handler
        self.pipe.connect(f'\\\\?\\pipe\\basembeddedpipes{pid}',
                          lambda pipe_handle, _: pipe_handle.start_read(self.handle))
        self.pipe.loop.run()

    def handle(self, _handle, data, _error):
        check_process(data)

        self.buffer += data.decode('utf-8')
        chunk = self.buffer.split(BOUNDARY)
        if len(chunk[-1]) != 0:
            self.buffer = chunk.pop()
        else:
            self.buffer = ''

        for item in chunk: self.handler(item)

    def write(self, obj, need_delete=True):
        if need_delete:
            obj['v'].pop(NEED_STOP, None)
        packet = json.dumps(obj) + BOUNDARY
        self.pipe.write(str.encode(packet))
