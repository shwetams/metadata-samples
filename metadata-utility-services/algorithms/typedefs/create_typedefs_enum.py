'''
1.defaultValue
2. elementDefs
    2.1 description
    2.2 ordinal
    2.3 value
3. category
4. createTime
5. createdBy
6. dateFormatter
7. description
8. guid
9. name
10. options
11. typeVersion
12. updateTime
13. updatedBy
14. version
'''



import atlas_enumdefs as atlas_enumdefs
import time

def create_enum_defs(enum_defs):
    enum_defs_list = []
    
    for enum_def in enum_defs:
        if enum_def.get("name") is not None and enum_def.get("elementDefs") is not None:
            enum_d = {}
            enum_d["name"] = enum_def["name"]
            enum_d["elementDefs"] = []
            for element in enum_def["elementDefs"]:
                enum_d["elementDefs"].append(element)
            enum_d["category"] = atlas_enumdefs.Category.ENUM.name
            if enum_def.get("guid") is not None:
                enum_d["guid"] = enum_def["guid"]
            if enum_def.get("createTime") is not None:
                enum_d["createTime"] = enum_def["createTime"]
            else:
                enum_d["createTime"] = int(time.time())
            if enum_def.get("createdBy") is not None:
                enum_d["createdBy"] = enum_def["createdBy"]
            else:
                enum_d["createdBy"] = "admin"
            if enum_def.get("updateTime") is not None:
                enum_d["updateTime"] = enum_def["updateTime"]
            else:
                enum_d["updateTime"] = int(time.time())
            if enum_def.get("updatedBy") is not None:
                enum_d["updatedBy"] = enum_def["updatedBy"]
            else:
                enum_d["updatedBy"] = int(time.time())
            if enum_def.get("createTime") is not None:
                enum_d["createTime"] = enum_def["createTime"]
            else:
                enum_d["createTime"] = int(time.time())
            if enum_def.get("typeVersion") is not None:
                enum_d["typeVersion"] = enum_def["typeVersion"]
            else:
                enum_d["typeVersion"] ="1.0"
            if enum_def.get("version") is not None:
                enum_d["version"] = enum_def["version"]
            else:
                enum_d["version"] = 1
            if enum_def.get("options") is not None:
                enum_d["options"] = enum_def["options"]
            enum_defs_list.append(enum_d)
    
    return enum_defs_list