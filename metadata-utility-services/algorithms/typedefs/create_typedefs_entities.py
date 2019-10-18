## Sample structure:
'''
1. entityDefs []
2. subTypes [string]
3. superTypes [string]
4. attributeDefs
    4.1 defaultValue
    4.2 description
    4.3 includeInNotification
    4.4 isIndexable
    4.5 isOptional
    4.6 isUnique
    4.7 name
    4.8 options
    4.9 typeName
    4.10 valuesMaxCount
    4.11 valuesMinCount
    4.12 cardinality := SINGLE, LIST, SET (ENUM)
    4.13 Array<constraints> 
        4.12.1 params []
            4.12.2 property1, value1 

5. category = "ENTITY"  (Enum type: PRIMITIVE, OBJECT_ID_TYPE, ENUM, STRUCT, CLASSIFICATION, ENTITY, ARRAY, MAP, RELATIONSHIP
6. createdBy
7.  dateFormatter
8. description
9. guid
10. name
11. options
12. updateTime
13. updatedBy
14. version

'''
## imports
import json

import atlas_enumdefs as atlas_enumdefs

import time

### Add any default attributes that need to be added for every entity 
mandatory_attribute_defs = []


def create_entity_defs(entity_defs):
    
    entity_defs_list = []
    for entity_def in entity_defs:
        if entity_def.get("name") is not None:
            entity= {}
            entity["name"] = entity_def["name"]
            if entity_def.get("description") is not None:
                entity["description"] = entity_def["description"]
            else:
                entity["description"] = entity_def["name"]
            if entity_def.get("superTypes") is not None:
                entity["superTypes"] = entity_def["superTypes"]
            else:
                entity["superTypes"] = []
            if entity_def.get("subTypes") is not None:
                entity["subTypes"] = entity_def["subTypes"]
            else:
                entity["subTypes"] = []
            entity["attributeDefs"] = []
            if entity_def.get("attributeDefs") is not None:
                for attribute in entity_def["attributeDefs"]:
                    if attribute.get("name") is not None and attribute.get("typeName") is not None and attribute.get("cardinality") is not None:
                        entity["attributeDefs"].append(attribute)
            if len(mandatory_attribute_defs) > 0:
                for mandatory_attribute in mandatory_attribute_defs:
                    entity["attributeDefs"].append(mandatory_attribute)

            entity["category"] = atlas_enumdefs.Category.ENTITY.name

            ### Optional 
            if entity_def.get("guid") is not None:
                entity["guid"] = entity_def["guid"]
            if entity_def.get("options") is not None:
                entity["options"] = entity_def["options"]
            if entity_def.get("createdBy") is not None:
                entity["createdBy"] = entity_def["createdBy"]
            else:
                entity["createdBy"] = "admin"
            if entity_def.get("updatedBy") is not None:
                entity["updatedBy"] = entity_def["updatedBy"]
            if entity_def.get("created_time") is not None:
                entity["createdTime"] = entity_def["createdTime"]
            else:
                entity["createdTime"] = int(time.time())
            if entity_def.get("updated_time") is not None:
                entity["updatedTime"] = entity_def["updatedTime"]
            else:
                entity["updatedTime"] = int(time.time())
            if entity_def.get("version") is not None:
                entity["version"] = int(entity_def["version"])
            else:
                entity["version"] = 1
            if entity_def.get("typeVersion") is not None:
                entity["typeVersion"] = entity_def["typeVersion"]
            else:
                entity["typeVersion"] = "1.0"
        entity_defs_list.append(entity)
    
    return entity_defs_list