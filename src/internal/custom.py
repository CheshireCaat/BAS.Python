import os

from internal.loader import Loader

SILENT_STOP = '-BAS-SILENT-STOP-'
NEED_STOP = '-BAS-NEED-STOP'

FUNCTIONS = {}


class PythonCustom:

    def __init__(self):
        pass

    def function_exist(self, func):
        return func in FUNCTIONS

    def clear_test_data(self, obj):
        obj['v'].pop(NEED_STOP, None)

    def init(self):
        path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '../custom'))

        for f in os.listdir(path):
            function_name = f.split('.')[0]

            if function_name == '__pycache__':
                continue
            if function_name == '__init__':
                continue

            function_path = os.path.join(path, f)
            FUNCTIONS[function_name] = Loader.import_module(function_path)

    def call(self, callback_api, callback_print, callback, data, obj):
        call_name, call_vars, call_key = obj['f'], obj['v'], obj['id']

        call_vars[NEED_STOP] = False
        data[call_key] = call_vars

        try:
            FUNCTIONS[call_name].invoke(call_vars, callback_api, callback_print)
            del data[call_key]
            if not call_vars[NEED_STOP]:
                callback(None)
        except Exception as e:
            print(str(e))
            del data[call_key]
            if not call_vars[NEED_STOP] and str(e) != SILENT_STOP:
                callback(str(e))
