import logging
import algorithms.atlas_qns as atlas_qns
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('Python HTTP trigger function processed a request.')
        logging.info(req.method)
        
        if req.method == "GET":
            typeName = req.params.get('typeName')
            required_inputs = atlas_qns.get_list_inputs(typeName)
            if len(required_inputs) == 0 or required_inputs == None:
                return func.HttpResponse(f"given typeName {typeName} is not recognised, please check the typeName entered",status_code=404) 
            else:
                required_input_out = json.dumps(required_inputs) 
                return func.HttpResponse(required_input_out,status_code=200,mimetype="application/json")
        if req.method == "POST":
            req_body = req.get_json()
            typeName = req.params.get("typeName")
            qualified_name_details = atlas_qns.get_qualified_name(typeName,req_body)
            output = json.dumps(qualified_name_details)
            return func.HttpResponse(output,status_code=200,mimetype="application/json")
    except Exception as e:
        logging.error(str(e))
        output = {}
        output["error_no"] = 500
        output["error_description"] = str(e)        
        return func.HttpResponse(json.dumps(output),status_code=500,mimetype="application/json")

        

    
'''
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
'''