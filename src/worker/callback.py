import json

from ..internal import custom
from ..internal import pipes


class Callback(object):
    api_callbacks = {}
    api_data = {}

    def __init__(self):
        self.custom = custom.Custom()
        self.pipe = pipes.Pipes()

    def callback_internal(self, obj, callback, api):
        key, obj['a'] = obj['id'], api
        self.api_callbacks[key] = callback
        self.pipe.write(obj)

    def callback_print(self, obj, message):
        try:
            send = {'l': json.dumps(message), 'id': obj['id']}
        except TypeError:
            send = {'l': 'undefined', 'id': obj['id']}
        self.pipe.write(send, False)

    def callback_data(self, obj, error):
        if error is not None:
            obj['e'] = error
            obj['s'] = False
        else:
            obj['e'] = ''
            obj['s'] = True
        self.pipe.write(obj)
