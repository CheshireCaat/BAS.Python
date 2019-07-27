from internal.custom import PythonCustom
from internal.pipe import PythonPipe
from internal.proc import PythonProc
import json
import sys

api_call = {}
api_data = {}


class PythonEmbedded:

    def start(self):
        self.custom.init()
        self.proc.init(sys.argv[2])
        self.pipe.init(sys.argv[2], self.handle)

    def callback_api(self, obj, api, callback):
        obj['a'] = api
        api_call[obj['id']] = callback
        self.custom.clear_test_data(obj)
        self.pipe.write(json.dumps(obj))

    def callback_print(self, obj, log):
        try:
            send = {}
            if type(obj) == object:
                send['l'] = json.dumps(log)
            else:
                send['l'] = str(log)
            send['id'] = obj['id']
            self.pipe.write(json.dumps(send))
        except Exception:
            send = {'l': 'undefined', 'id': obj['id']}
            self.pipe.write(json.dumps(send))

    def callback(self, obj, err = None):
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
                self.pipe.write(json.dumps(obj));
                return

            self.custom.call(
                self.callback_print,
                self.callback_api,
                self.callback,
				obj['f'],
                obj['v'],
                obj['id'],
                api_data,
                obj
            )

        # Return api
        if obj['t'] == 1:
            if not obj['id'] in api_call:
                obj['e'] = 'Task id not found'
                obj['s'] = False
                self.custom.clear_test_data(obj)
                self.pipe.write(json.dumps(obj))
                return
            call = api_call[obj['id']]
            del api_call[obj['id']]
            call(obj['v'], False)

        # Kill task
        if obj['t'] == 2:
            if obj['id'] in api_call:
                call = api_call[obj['id']]
                del api_call[obj['id']]
                call(obj['v'], True)
            if obj['id'] in api_data:
                data = api_data[obj['id']]
                data['-BAS-NEED-STOP-'] = True

        # Stats
        if obj['t'] == 3:
            res = {
                's1': len(api_data),
                's2': len(api_call)
            }
            self.pipe.write(json.dumps(res))

    def __init__(self):
        self.custom = PythonCustom()
        self.pipe = PythonPipe()
        self.proc = PythonProc()


if __name__ == '__main__':
    PythonEmbedded().start()
