import atlas_enumdefs as atlas_enumdefs
import time
import json
'''
1. category	TypeCategory	
2. createTime	number	
3. createdBy	string	
4. dateFormatter	DateFormat	
5. description	string	
6. guid	string	
7. name	string	
8. options	map of string	
9. serviceType	string	
10. typeVersion	string	
11. updateTime	number	
12. updatedBy	string	
13. version	number
14. attributeDefs
        14.1 name
        14.2 typeName
        14.3 isOptional
        14.4 cardinality
        14.5 valuesMinCount
        14.6 valuesMaxCount
        14.7 isUnique
        14.8 isIndexable
        14.9 includeInNotification

'''



def create_struct_defs(structDefs):
    struct_defs_list = []
    for structDef in structDefs:
        struct_def = {}
        if structDef.get("name") is not None and structDef.get("attributeDefs") is not None:
            struct_def["category"] = atlas_enumdefs.Category.STRUCT.name
            struct_def["attributeDefs"] = []
            struct_def["name"] = structDef["name"]
            if structDef.get("attributeDefs") is not None:
                for attribute in structDef["attributeDefs"]:
                    if attribute.get("name") is not None and attribute.get("typeName") is not None:
                        struct_def["attributeDefs"].append(attribute)
            if structDef.get("guid") is not None:
                struct_def["guid"] = structDef["guid"]
            if structDef.get("createTime") is not None:
                struct_def["createTime"] = structDef["createTime"]
            else:
                struct_def["createTime"] = int(time.time())
            if structDef.get("createdBy") is not None:
                struct_def["createdBy"] = structDef["createdBy"]
            else:
                struct_def["createdBy"] = "admin"
            if structDef.get("updateTime") is not None:
                struct_def["updateTime"] = structDef["updateTime"]
            else:
                struct_def["updateTime"] = int(time.time())
            if structDef.get("updatedBy") is not None:
                struct_def["updatedBy"] = structDef["updatedBy"]
            else:
                struct_def["updatedBy"] = "admin"
            if structDef.get("description") is not None:
                struct_def["description"] = structDef["description"]
            else:
                struct_def["description"] = structDef["name"]
            if structDef.get("options") is not None:
                struct_def["options"] = structDef["options"]
            if structDef.get("serviceType") is not None:
                struct_def["serviceType"] = structDef["serviceType"]
            if structDef.get("typeVersion") is not None:
                struct_def["typeVersion"] = structDef["typeVersion"]
            else:
                struct_def["typeVersion"] = "1.0"
            struct_defs_list.append(struct_def)
    return struct_defs_list        
