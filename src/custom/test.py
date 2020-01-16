
def invoke(_bas_vars, _bas_api, _bas_print):
    bas_print = _bas_print
    bas_vars = _bas_vars
    bas_api = _bas_api

    from src.testa import testa as test_a
    from src.testb import testb as test_b

    bas_print(test_a())
    bas_print(test_b())
