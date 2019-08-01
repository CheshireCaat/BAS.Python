from importlib import util
from os import pardir, path, walk


class Loader:

    @staticmethod
    def import_functions():
        for filename in Loader.list_modules(custom=True):
            file = path.basename(filename)
            name = file.split('.')[0]

            if '__pycache__' in filename:
                continue

            if '__init__' in filename:
                continue

            yield name, Loader.__load_module(filename)

    @staticmethod
    def import_module(name):
        for filename in Loader.list_modules(custom=False):
            if '__pycache__' in filename:
                continue

            if '__init__' in filename:
                continue

            if not name in filename:
                continue

            return Loader.__load_module(filename)

    @staticmethod
    def list_modules(custom=False):
        if custom is True:
            def_path = path.join(path.dirname(__file__), '../custom')
            for dir, _, files in walk(def_path):
                for file in files:
                    yield path.abspath(path.join(dir, file))
        else:
            def_path = path.join(path.dirname(__file__), pardir)
            for dir, _, files in walk(def_path):
                for file in files:
                    yield path.abspath(path.join(dir, file))

    @staticmethod
    def __load_module(file):
        name = path.basename(file)
        spec = Loader.__load_spec(name, file)
        func = Loader.__load_func(spec)
        spec.loader.exec_module(func)
        return func

    @staticmethod
    def __load_spec(name, path):
        return util.spec_from_file_location(name, path)

    @staticmethod
    def __load_func(spec):
        return util.module_from_spec(spec)
