'''
RelationshipDefs
1. name
2. guid
3. relationshipCategory ( ASSOCIATION, AGGREGATION, COMPOSITION )
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
3. end1Def
    3.1 cardinality 
    3.2 isContainer
    3.3 isLegacyAttribute
    3.4 name
    3.5 type 
4. end2Def
    4.1 cardinality
    4.2 isContainer
    4.3 isLegacyAttribute
    4.4 name
    4.5 type
5. createdBy
7.  dateFormatter
8. description
9. options
11. updateTime
12. updatedBy
13. version
14. category 
15. propagateTags (NONE, ONE_TO_TWO, TWO_TO_ONE, BOTH )
16. relationshipLabel

 '''


import atlas_enumdefs as atlas_enumdefs
import time



## Any attributes that need to be added to every relationship
mandatory_relationship_attributes = []



def create_relationship_defs(relationship_defs):
    
    relationship_defs_list = []
    for relationship_def in relationship_defs:
        if relationship_def.get("name") is not None and relationship_def.get("endDef1") is not None and relationship_def.get("endDef2") is not None and relationship_def.get("relationshipCategory") is not None:
            end1Def = relationship_def["endDef1"]
            end2Def = relationship_def["endDef2"]
            if end1Def.get("name") is not None and end1Def.get("type") is not None and end1Def.get("cardinality") is not None and end2Def.get("name") is not None and end2Def.get("type") is not None and end2Def.get("cardinality"):
                ## All mandatory values present
                relationship = {}
                relationship["name"] = relationship_def["name"]
                relationship["relationshipCategory"] = relationship_def["relationshipCategory"]
                relationship["endDef1"] = relationship_def["endDef1"]
                relationship["endDef2"] = relationship_def["endDef2"]
                if relationship_def.get("description") is not None:
                    relationship["description"]= relationship_def["description"]
                else:
                    relationship["description"] = relationship_def["name"]
                if relationship_def.get("propagateTags") is not None:
                    relationship["propagateTags"] = relationship_def["propagateTags"]
                else:
                    relationship["propagateTags"] = atlas_enumdefs.relationship_propagateTags.NONE.name
                if relationship_def.get("createTime") is not None:
                    relationship["createTime"] = relationship_def["createTime"]
                else:
                    relationship["createTime"] = int(time.time())
                if relationship_def.get("updateTime") is not None:
                    relationship["updateTime"] = relationship_def["updateTime"]
                else:
                    relationship["updateTime"] = int(time.time())
                if relationship_def.get("createdBy") is not None:
                    relationship["createdBy"] = relationship_def["createdBy"]
                else:
                    relationship["createdBy"] = "admin"
                if relationship_def.get("relationshipLabel") is not None:
                    relationship["relationshipLabel"] = relationship_def["relationshipLabel"]
                else:
                    relationship["relationshipLabel"] = str("r:" + relationship_def["name"])
                if relationship_def.get("guid") is not None:
                    relationship["guid"] = relationship_def["guid"]
                relationship["category"] = atlas_enumdefs.Category.RELATIONSHIP.name
                relationship_defs_list.append(relationship)
    
    return relationship_defs_list
                



