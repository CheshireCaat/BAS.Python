BAS_VARS =None
BAS_API = None
BAS_LOG = None

def invoke(m_bas_vars, m_bas_api, m_bas_log):
	#var BAS_API = async (API_STRING) => {
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
	#}
	#var BAS_PERHAPS_STOP = () => {
	#	if(BAS_VARS["-BAS-NEED-STOP-"])
	#		throw "-BAS-SILENT-STOP-"
	#}
    BAS_VARS = m_bas_vars
    BAS_API = m_bas_api
    BAS_LOG = m_bas_log

    BAS_LOG(BAS_VARS['VAR_1'])
    print(BAS_VARS['VAR_1'])