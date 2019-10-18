import json
import algorithms.create_entity as create_entity

## Sample Input
process = {}
process["guid"]="3134b5cc-60a3-43b4-815a-bdf99fd81263"
process["name"] = "derived_from_col_dq"
process["type_name"] = "derived_from_col"
process["qualified_name"] = "process/derived_from_col/dqrule/azure_sql_column"
process["created_by"] = "sg"
process["process_attributes"] = []
process["process_attributes"].append({"attr_name":"StartTime", "attr_value":"10:40:09","is_entityref":False})
process["process_attributes"].append({"attr_name":"EndTime","attr_value":"10:50:09","is_entityref":False})
process["inputs"] = []
process["outputs"] = []
process["outputs"].append({"guid":"faf02429-9fbf-4d97-b0d9-35a8dd6887bd","typeName":"DQ_Rule_1"})
process["outputs"].append({"guid":"674aeda1-6f7d-4d61-9910-188b9050ed52","typeName":"DQ_Rule_1"})
process["inputs"].append({"guid":"ddb2bc49-af2a-41e3-9b26-0c6bec90e0d6","typeName":"azure_sql_column_sg"})
print(json.dumps(process))

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
