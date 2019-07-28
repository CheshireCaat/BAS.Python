from importlib import util

class Loader:

    @staticmethod
    def import_module(name, path):
        spec = Loader.__spec_from_file(name,path)
        func = Loader.__func_from_spec(spec)
        spec.loader.exec_module(func)
        return func

    @staticmethod
    def __spec_from_file(name, path):
        return util.spec_from_file_location(name, path)

    @staticmethod
    def __func_from_spec(spec):
        return util.module_from_spec(spec)