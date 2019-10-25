import json
#import http.client
import requests
import urllib.parse
import os

qns_typename_json = "algorithms/qns-typename-lookup.json"
#atlas_api_wrapper_url_ev = "ATLAS_WRAPPER_URL"

#os.environ["ATLAS_WRAPPER_URL"]="https://atlasapiwrapper.azurewebsites.net/api/search"
atlas_api_wrapper_url = "https://atlasapiwrapper.azurewebsites.net/api/search?query="
#atlas_api_wrapper_url = os.environ.get(atlas_api_wrapper_url_ev)
## for testing Atlas URL


# Get the list of resources

def get_list_inputs(typeName):
    param_details = {}
    with open(qns_typename_json) as qns_file:
        qns_list = json.load(qns_file)
        for qns in qns_list:
            if qns.get("typeName") is not None:
                if typeName == qns["typeName"]:
                    param_details["pattern"] = qns["pattern"]
                    param_details["input_parameters"] = qns["input_parameters"]
                    param_details["input_format"] = "[{param_name:param_value},....{param_name:param_value}]"
                    param_details["description"] = "The service will return a null guid if the qualified name does not exists in Atlas, check for error code for any errors"
        qns_file.close()
    return param_details

def get_qualified_name(typeName, input_params):
    ## Check if input parameters are present
    output = {}
    output["error_code"] = 0
    output["error_description"]=""
    required_inputs = get_list_inputs(typeName)
    allParamsExists = True
    missingParams = []
    for input in required_inputs["input_parameters"]:
        if input["param_name"] not in input_params.keys():
            allParamsExists = False
            missingParams.append(input["name"])
    if allParamsExists is True:
        if required_inputs.get("pattern") is not None:
            # Build the qualified name
            qualifiedName = create_qualified_name(typeName,input_params,required_inputs)
            # Check if qualified name exists and return the output
            output = verify_qualified_name(typeName,qualifiedName)
        else:
            output["error_code"] = 101
            output["error_description"] = "Pattern not found for this typeName, please ensure you are providing a valid typeName defined in Atlas and configured"
        
    else:
        output["error_code"] = 100
        output["error_description"] = "Missing Parameters" + json.dumps(missingParams)
    return output

def create_qualified_name(typeName, input_params,required_inputs):
    qualified_name = required_inputs["pattern"]
    for inputs in required_inputs["input_parameters"]:
        param_name = inputs["param_name"]
        param_value = input_params[param_name]
        qualified_name = str(qualified_name).replace("{"+str(param_name)+"}",param_value)
        qualified_name = str(qualified_name).lower()
    return qualified_name

def verify_qualified_name(typeName, qualifiedName):
    qualifiedNameDetails = {}
    qualifiedNameDetails["isExists"] = False
    qualifiedNameDetails["qualifiedName"] = qualifiedName
    qualifiedNameDetails["guid"] = None
    qualifiedNameDetails["error_code"] = 0
    qualifiedNameDetails["error_description"] = ""
    query = urllib.parse.quote("from "+ str(typeName) + "+where+qualifiedName="+ str(qualifiedName))
    if atlas_api_wrapper_url is not None:
        url = atlas_api_wrapper_url+query
        req = requests.get(url=url)
        if req.status_code == 200:
            data = req.json()
            for entity in data["entities"]:
                e_typeName = entity.get("typeName")
                e_attributes = {}
                e_attributes = entity.get("attributes")
                if e_typeName == typeName and e_attributes.get("qualifiedName") == qualifiedName:
                    qualifiedNameDetails["isExists"] = True
                    qualifiedNameDetails["guid"] = entity.get("guid")
        else:
            if req.status_code is not 404:
                qualifiedNameDetails["error_code"] = 103
                qualifiedNameDetails["error_description"] = str(req.status_code) + req.reason
    else:
        qualifiedNameDetails["error_code"] = 104
        qualifiedNameDetails["error_description"] = "Cannot find Atlas API Environment variable"
    return qualifiedNameDetails


#input_params = {"azure_sql_server_uri":"asset","database_name":"categoryid11"}
#print(json.dumps(get_qualified_name("azure_sql_column_sg",input_params)))