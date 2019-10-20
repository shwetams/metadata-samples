import logging

import azure.functions as func
import algorithms.json_generator_algorithms as algorithms
import json


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Creating entity.')
    swagger_link = "https://app.swaggerhub.com/apis/shwetams/apache-atlas-json-generator-entity/0.1"
    req_body = req.get_json()
    logging.info(f'Creating relationship.{req}')
    print(req_body)
    relationship_json = algorithms.create_relationships_def(req_body)
    if relationship_json is not None:
        return func.HttpResponse(json.dumps(relationship_json),status_code=200,mimetype="application/json")
    else:
        return func.HttpResponse(f"Invalid Entity structure please use the structure defined in the link {swagger_link}",status_code=400)
    
