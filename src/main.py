import json
import sys

from src.internal.constants import NEED_STOP
from src.worker.callback import Callback


class Worker(Callback):

    def __init__(self):
        super().__init__()
        self.handler = {
            0: self.handle_run,
            1: self.handle_api,
            2: self.handle_task,
            3: self.handle_stats
        }

    def handle_stats(self, obj):
        obj = {
            's2': len(self.api_callbacks),
            's1': len(self.api_data)
        }
        self.pipe.write(obj, False)

    def handle_task(self, obj):
        if obj['id'] in self.api_callbacks:
            callback = self.api_callbacks[obj['id']]
            del self.api_callbacks[obj['id']]
            callback(obj['v'], True)
        if obj['id'] in self.api_data:
            data = self.api_data[obj['id']]
            data[NEED_STOP] = True

    def handle_api(self, obj):
        if not obj['id'] in self.api_callbacks:
            obj['e'] = 'Task id not found'
            obj['s'] = False
            self.pipe.write(obj)
            return
        call = self.api_callbacks.pop(obj['id'])
        call(obj['v'], False)

    def handle_run(self, obj):
        if self.custom.find(obj['f']):
            self.custom.call(
                lambda error: self.callback_data(obj, error),
                lambda message: self.callback_print(obj, message),
                lambda callback, api: self.callback_internal(obj, callback, api),
                self.api_data,
                obj
            )
            return
        obj['e'], obj['s'] = 'Function ' + obj['f'] + ' not exists', False
        self.pipe.write(obj)

    def handle(self, data):
        try:
            obj = json.loads(data)
            self.handler[obj['t']](obj)
        except ValueError:
            return

    def run(self):
        self.pipe.run(self.handle, sys.argv[1])


if __name__ == '__main__':
    worker = Worker()
    worker.run()
