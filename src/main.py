import json
import sys

from src.internal.custom import PythonCustom
from src.internal.pipe import PythonPipe

API_CALLBACKS = {}
API_OBJECTS = {}


class PythonEmbedded:

    def __init__(self):
        self.custom = PythonCustom()
        self.pipe = PythonPipe()

    def start(self):
        self.custom.init()
        self.pipe.init(self.handle)

    def callback_api(self, obj, api, callback):
        obj['a'] = api
        API_CALLBACKS[obj['id']] = callback
        self.custom.clear_test_data(obj)
        self.pipe.write(json.dumps(obj))

    def callback_print(self, obj, log):
        try:
            send = {
                'l': json.dumps(log),
                'id': obj['id']
            }
            self.pipe.write(json.dumps(send))
        except TypeError:
            send = {
                'l': 'undefined',
                'id': obj['id']
            }
            self.pipe.write(json.dumps(send))

    def callback_func(self, obj, err):
        if err is not None:
            obj['e'] = err
            obj['s'] = False
        else:
            obj['e'] = ''
            obj['s'] = True
        self.custom.clear_test_data(obj)
        self.pipe.write(json.dumps(obj))

    def handle(self, data):
        try:
            obj = json.loads(data)
        except ValueError:
            obj = None

        if obj is None:
            return

        # Run new function
        if obj['t'] == 0:
            if not self.custom.function_exist(obj['f']):
                obj['e'] = 'Function ' + obj['f'] + ' not exists'
                obj['s'] = False
                self.custom.clear_test_data(obj)
                self.pipe.write(json.dumps(obj))
                return

            self.custom.call(
                lambda x, y: self.callback_api(obj, x, y),
                lambda x: self.callback_print(obj, x),
                lambda x: self.callback_func(obj, x),
                API_OBJECTS,
                obj
            )

        # Return api
        if obj['t'] == 1:
            if not obj['id'] in API_CALLBACKS:
                obj['e'] = 'Task ' + obj['id'] + ' not exist'
                obj['s'] = False
                self.custom.clear_test_data(obj)
                self.pipe.write(json.dumps(obj))
                return
            call = API_CALLBACKS[obj['id']]
            del API_CALLBACKS[obj['id']]
            call(obj['v'], False)

        # Kill task
        if obj['t'] == 2:
            if obj['id'] in API_CALLBACKS:
                call = API_CALLBACKS[obj['id']]
                del API_CALLBACKS[obj['id']]
                call(obj['v'], True)
            if obj['id'] in API_OBJECTS:
                data = API_OBJECTS[obj['id']]
                data['-BAS-NEED-STOP-'] = True

        # Stats
        if obj['t'] == 3:
            res = {
                's2': len(API_CALLBACKS),
                's1': len(API_OBJECTS)
            }
            self.pipe.write(json.dumps(res))


if __name__ == '__main__':
    PythonEmbedded().start()
