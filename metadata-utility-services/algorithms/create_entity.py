import json
# Input:
input_entities = []
# DQ Rule 1
input_entity1 = {}
input_entity1["entity_type_name"]="DQ_Rule_1"
input_entity1["created_by"]="sg"
attributes1 = []
attributes1.append({"attr_name":"qualifiedName","attr_value":"dq_rules/day_date/notnull","is_entityref":False})
attributes1.append({"attr_name":"name","attr_value":"Not Null Check of Day Date","is_entityref":False})
attributes1.append({"attr_name":"rule_type","attr_value":"NotNull","is_entityref":False})
attributes1.append({"attr_name":"rule_id","attr_value":"rule101","is_entityref":False})
input_entity1["attributes"]=attributes1
#print(input_entity1)

# DQ Rule 2
input_entity2 = {}
input_entity2["entity_type_name"]="DQ_Rule_1"
input_entity2["created_by"]="sg"
attributes2 = []
attributes2.append({"attr_name":"qualifiedName","attr_value":"dq_rules/day_key/uniquenesscheck","is_entityref":False})
attributes2.append({"attr_name":"name","attr_value":"Uniqueness Check of Day Key","is_entityref":False})
attributes2.append({"attr_name":"rule_type","attr_value":"UniquenessCheck","is_entityref":False})
attributes2.append({"attr_name":"rule_id","attr_value":"rule102","is_entityref":False})
input_entity2["attributes"]=attributes2
#print(input_entity2)

# azure sql column
input_entity3 = {}
input_entity3["entity_type_name"]="azure_sql_column"
input_entity3["created_by"]="sg"
attributes3 = []
attributes3.append({"attr_name":"qualifiedName","attr_value":"asset/categoryid","is_entityref":False})
attributes3.append({"attr_name":"name","attr_value":"CategoryID","is_entityref":False})
attributes3.append({"attr_name":"data_type","attr_value":"string","is_entityref":False})
attributes3.append({"attr_name":"FailedCount","attr_value":2000,"is_entityref":False})
attributes3.append({"attr_name":"TotalCount","attr_value":10000000,"is_entityref":False})
attributes3.append({"attr_name":"DQRules","attr_value":[{"guid":"faf02429-9fbf-4d97-b0d9-35a8dd6887bd","typeName":"DQ_Rule_1","uniqueAttributes":{}},{"guid":"674aeda1-6f7d-4d61-9910-188b9050ed52","typeName":"DQ_Rule_1","uniqueAttributes":{}}],"is_entityref":True})
input_entity3["attributes"]=attributes3
#print(input_entity3)

input_entities.append(input_entity1)
input_entities.append(input_entity2)
input_entities.append(input_entity3)
print(json.dumps(input_entities))

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


#create_entity_def(input_entities)
