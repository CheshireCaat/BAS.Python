from loader import Loader
import os

SILENT_STOP = '-BAS-SILENT-STOP-'
NEED_STOP = '-BAS-NEED-STOP'

functions = {}


class PythonCustom:

    def function_exist(self, func):
        return func in functions

    def clear_test_data(self, obj):
        obj['v'].pop(NEED_STOP, None)

    def init(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../custom'))

        for f in os.listdir(path):
            function_name = f.split('.')[0]
            if not function_name.startswith('__'):
                function_path = os.path.join(path, f)
                functions[function_name] = Loader.import_module(function_name, function_path)
                
    def call(self, callback_api, callback_log, callback, data, obj):
        name = obj['f']
        vars = obj['v']
        key = obj['id']

        vars[NEED_STOP] = False
        data[key] = vars
        try:
            functions[name].invoke(vars, callback_api, callback_log)
            del data[key]
            if not vars[NEED_STOP]:
                callback(None)
        except Exception as e:
            del data[key]
            if not vars[NEED_STOP] and str(e) != SILENT_STOP:
                callback(str(e))
