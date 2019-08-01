import os

from src.internal.loader import Loader

SILENT_STOP = '-BAS-SILENT-STOP-'
NEED_STOP = '-BAS-NEED-STOP'

functions = {}


class PythonCustom:

    def __init__(self):
        pass

    def function_exist(self, func):
        return func in functions

    def clear_test_data(self, obj):
        obj['v'].pop(NEED_STOP, None)

    def init(self):
        for name, func in Loader.import_functions():
            functions[name] = func

    def call(self, callback_api, callback_print, callback, data, obj):
        call_name, call_vars, call_key = obj['f'], obj['v'], obj['id']

        call_vars[NEED_STOP] = False
        data[call_key] = call_vars

        try:
            functions[call_name].invoke(
                call_vars, callback_api, callback_print)
            del data[call_key]
            if not call_vars[NEED_STOP]:
                callback(None)
        except Exception as e:
            del data[call_key]
            if not call_vars[NEED_STOP] and str(e) != SILENT_STOP:
                callback(str(e))
