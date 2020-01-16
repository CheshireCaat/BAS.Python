import glob
import threading
from importlib import util
from os.path import splitext, basename, dirname, join

from .constants import NEED_STOP, SILENT_STOP

modules = {}


class Custom:

    def __init__(self):
        def_path = join(dirname(__file__), '../custom')
        for file in glob.glob(join(def_path, "*.py")):
            name = splitext(basename(file))[0]
            spec = util.spec_from_file_location(name, file)
            module = util.module_from_spec(spec)
            spec.loader.exec_module(module)
            modules[name] = module

    @staticmethod
    def find(func):
        return func in modules

    @staticmethod
    def call(callback, callback_print, callback_api, api_data, obj):
        variables, name, key = obj['v'], obj['f'],  obj['id']

        def wrap():
            try:
                modules[name].invoke(
                    variables, callback_api, callback_print)
                del api_data[key]
                if not variables[NEED_STOP]:
                    callback(None)
            except Exception as e:
                del api_data[key]
                if not variables[NEED_STOP] and str(e) != SILENT_STOP:
                    callback(str(e))

        variables[NEED_STOP] = False
        api_data[key] = variables

        thread = threading.Thread(target=wrap)
        thread.run()
