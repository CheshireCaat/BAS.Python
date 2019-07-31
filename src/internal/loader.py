import os
from importlib import util


class Loader:

    @staticmethod
    def import_module(path):
        name = os.path.basename(path)
        spec = Loader.__load_spec(name, path)
        func = Loader.__load_func(spec)
        spec.loader.exec_module(func)
        return func

    @staticmethod
    def list_modules(folder=None):
        if folder is None:
            def_path = os.path.join(os.path.dirname(__file__), os.pardir)
        else:
            def_path = os.path.join(os.path.dirname(__file__), folder)
        return os.listdir(os.path.abspath(def_path))

    @staticmethod
    def __load_spec(name, path):
        return util.spec_from_file_location(name, path)

    @staticmethod
    def __load_func(spec):
        return util.module_from_spec(spec)
