import json
from enum import Enum
import time
import algorithms.create_entity as create_entity

user_name = "admin"
class relationship_status(Enum):
    ACTIVE = 1
    DELETED = 2
    
## Creating Entities
def create_entity_def(input_entities):
    entities = []
    entities_def = {}
    for input_entity in input_entities:
        entity = {}
        if input_entity.get("entity_type_name") is not None:
            entity["typeName"] = input_entity["entity_type_name"] 
            if input_entity.get("guid") is not None:
                entity["guid"] = input_entity["guid"]
            if input_entity.get("created_by") is not None:
                entity["createdBy"]= input_entity["created_by"]
            attributes = {}
            if input_entity.get("attributes") is not None:
                for attribute in input_entity["attributes"]:
                    if attribute["is_entityref"]== False:
                        attributes[attribute["attr_name"]] = attribute["attr_value"] 
                    else:
                        attributes[attribute["attr_name"]] = []
                        for att_v in attribute["attr_value"]:
                            attributes[attribute["attr_name"]].append(att_v)
                entity["attributes"] = attributes
        entities.append(entity)
    entities_def = {"entities":entities}
    if len(entities) <= 0:
        entities_def = None
    return(entities_def)




## Creating relationships
def create_relationships_def(inp_relationships):
    relationships = []
    for inp_relationship in inp_relationships:
        if inp_relationship.get("name") is not None and inp_relationship["end1"] is not None and inp_relationship["end2"] is not None and inp_relationship["typeName"] is not None:
            relationship = {}
            # Mandatory Values
            relationship["name"] = inp_relationship["name"]
            relationship["end1"] = inp_relationship["end1"]
            relationship["end2"] = inp_relationship["end2"]
            relationship["typeName"] = inp_relationship["typeName"]
            # Optional Values
            if inp_relationship.get("blockedPropagatedClassifications") is not None:
                relationship["blockedPropagatedClassifications"] = inp_relationship["blockedPropagatedClassifications"]
            if inp_relationship.get("createTime") is not None:
                relationship["createTime"] = inp_relationship["createTime"]
            else:
                relationship["createTime"] = int(time.time())
            if inp_relationship.get("createdBy") is not None:
                relationship["createdBy"] = inp_relationship["createdBy"]
            else:
                relationship["createdBy"] = user_name
            if inp_relationship.get("guid") is not None:
                relationship["guid"] = inp_relationship["guid"]
            if inp_relationship.get("homeId") is not None:
                relationship["homeId"] = inp_relationship["homeId"]
            if inp_relationship.get("label") is not None:
                relationship["label"] = inp_relationship["label"]
            if inp_relationship.get("propagateTags") is not None:
                relationship["propagateTags"] = inp_relationship["propagateTags"]
            if inp_relationship.get("propagatedClassifications") is not None:
                relationship["propagatedClassifications"] = inp_relationship["propagatedClassifications"]
            if inp_relationship.get("status") is not None:
                relationship["status"] = inp_relationship["status"]
            else:
                relationship["status"] = relationship_status.ACTIVE.name
            if inp_relationship.get("updateTime") is not None:
                relationship["updateTime"] = inp_relationship["updateTime"]
            else:
                relationship["updateTime"] = int(time.time())
            if inp_relationship.get("version") is not None:
                relationship["version"] = inp_relationship["version"]
            if inp_relationship.get("attributes") is not None:
                relationship["attributes"] = inp_relationship["attributes"]
            if inp_relationship.get("updatedBy") is not None:
                relationship["updatedBy"] = inp_relationship["updatedBy"]
            else:
                relationship["updatedBy"] = user_name
            relationships.append(relationship)
    return relationships

## Creating lineage

def create_lineage_entity_def(process):
    lineage_entity_json = []
    lineage_entity = {}
    
    if process.get("name") is not None and process.get("qualified_name") is not None and process.get("inputs") is not None and process.get("outputs") is not None:
        lineage_entity["entity_type_name"] = process["type_name"]
        if process.get("guid") is not None:
            lineage_entity["guid"] = process["guid"]
           
        if process.get("created_by") is not None:
            lineage_entity["created_by"] = process["created_by"]
        else:
            lineage_entity["created_by"] = "admin"
        lineage_entity["attributes"] = []
        lineage_inputs = []
        for lineage_input in process["inputs"]:
            if lineage_input.get("guid") is not None and lineage_input.get("typeName") is not None:
                lineage_inputs.append(lineage_input)
        lineage_entity["attributes"].append({"attr_name":"inputs","attr_value":lineage_inputs,"is_entityref":False})
        lineage_outputs = []
        for lineage_output in process["outputs"]:
            if lineage_output.get("guid") is not None and lineage_output.get("typeName") is not None:
                lineage_outputs.append(lineage_output)
        lineage_entity["attributes"].append({"attr_name":"outputs","attr_value":lineage_outputs,"is_entityref":False})
        lineage_entity["attributes"].append({"attr_name":"qualifiedName","attr_value":process["qualified_name"],"is_entityref":False})
        lineage_entity["attributes"].append({"attr_name":"name","attr_value":process["name"],"is_entityref":False})
        if process.get("process_attributes") is not None:
            for process_attribute in process["process_attributes"]:
                if process_attribute.get("attr_name") is not None and process_attribute.get("attr_value") is not None:
                    if process_attribute.get("is_entityref") is not None:
                        lineage_entity["attributes"].append(process_attribute)
    lineage_entity_json.append(lineage_entity)
    lineage_atlas_json = create_entity.create_entity_def(lineage_entity_json)
    return lineage_atlas_json
