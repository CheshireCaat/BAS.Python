import importlib.machinery
import os

functions = {}


class PythonCustom:

    @staticmethod
    def function_exist(func):
        return func in functions

    @staticmethod
    def clear_test_data(obj):
        obj['v'].pop('-BAS-NEED-STOP-', None)

    @staticmethod
    def init():
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../custom'))

        for f in os.listdir(path):
            name = f.split('.')[0]
            if not name.startswith('__'):
                function_path = os.path.join(path, f)
                spec = importlib.util.spec_from_file_location(name, function_path)
                functions[name] = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(functions[name])

    @staticmethod
    def call(callback_print, callback_api, callback, name, variables, key, data, obj):
        variables['-BAS-NEED-STOP-'] = False
        data[key] = variables
        try:
            functions[name].test(variables)
            del data[key]
            if not variables['-BAS-NEED-STOP-']:
                callback(obj)
        except Exception as e:
            del data[key]
            if not variables['-BAS-NEED-STOP-'] and str(e) != '-BAS-SILENT-STOP-':
                callback(obj, str(e))
