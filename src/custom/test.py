from internal.loader import Loader

def invoke(m_bas_vars, m_bas_api, m_bas_log):
    # var BAS_API = async (API_STRING) => {
    #	let res = await BAS_API_INTERNAL(API_STRING);
    #	if(res[1])
    #		throw "-BAS-SILENT-STOP-";
    #	Object.assign(BAS_VARS, res[0]);
    #	BAS_VARS["-BAS-NEED-STOP-"] = false;
    #	if(BAS_VARS["-BAS-API-ERROR-"]) {
    #		var ex = BAS_VARS["-BAS-API-ERROR-"];
    #		delete BAS_VARS["-BAS-API-ERROR-"];
    #		throw ex;
    #	}
    # }
    # var BAS_PERHAPS_STOP = () => {
    #	if(BAS_VARS["-BAS-NEED-STOP-"])
    #		throw "-BAS-SILENT-STOP-"
    # }

    # bas_stop = lambda: if bas_vars['-BAS-NEED-STOP'] raise Exception('-BAS-SILENT-STOP')

    bas_vars = m_bas_vars
    bas_api = m_bas_api
    bas_log = m_bas_log

    test_a = Loader.import_module("E:/BAS Python/distr/src/testa.py")
    test_b = Loader.import_module("E:/BAS Python/distr/src/testb.py")

    test_a.testa()
    test_b.testb()

    bas_log(bas_vars['VAR_1'])
    bas_log(bas_vars)
    bas_log(invoke)
    bas_log(False)
    bas_log(2.5)
    bas_log(1)
