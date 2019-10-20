import logging
#import algorithms.create_lineage as create_lineage
import algorithms.json_generator_algorithms as algorithms
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:

    swagger_link = "https://app.swaggerhub.com/apis/shwetams/apache-atlas-json-generator-lineage/0.1"
    logging.info(f'Creating entity.{req}')
    req_body = req.get_json()
    print(req_body)
    entity_json = algorithms.create_lineage_entity_def(req_body)
    if entity_json is not None:
        return func.HttpResponse(json.dumps(entity_json),status_code=200,mimetype="application/json")
    else:
        return func.HttpResponse(f"Invalid Entity structure please use the structure defined in the link {swagger_link}",status_code=400)