
import create_typedefs_entities
import create_typedefs_relationships
import create_typedefs_enum
import create_typedefs_structs
import create_typedefs_classifications

import atlas_enumdefs
import json
## Sample input for entity:

entity_defs = []
entity_def = {}
entity_def["name"] ="azure_cosmosdb_account"
entity_def["description"] ="azure_cosmosdb_account"
entity_def["subTypes"] = [] # Array of strings or empty array
entity_def["superTypes"] = [] # Array of strings of empty array
entity_def["attributeDefs"] = [] # Array of attributes
attribute1 = {}
attribute1["name"] = "api_type"
attribute1["typeName"] = "string"
attribute1["isOptional"] = False
attribute1["cardinality"] = atlas_enumdefs.Cardinality.SINGLE.name
attribute1["valuesMinCount"] = 1
attribute1["valuesMaxCount"] = 1
attribute1["isUnique"] = False
attribute1["isIndexable"] = False
attribute1["includeInNotification"] = False
attribute2 = {}
attribute2["name"] = "ods_zone"
attribute2["typeName"] = "string"
attribute2["isOptional"] = False
attribute2["cardinality"] = atlas_enumdefs.Cardinality.SINGLE.name
attribute2["valuesMinCount"] = 1
attribute2["valuesMaxCount"] = 1
attribute2["isUnique"] = False
attribute2["isIndexable"] = False
attribute2["includeInNotification"] = False
entity_def["attributeDefs"].append(attribute1)
entity_def["attributeDefs"].append(attribute2)

#entity_def["category"] = atlas_enumdefs.Category.ENTITY.name
#entity_def["guid"] = -200
#entity_def["created_by"] = "admin"
#entity_def["updated_by"] = "admin"
#entity_def["createTime"] = 1566356848465
#entity_def["updateTime"] = 1566356848465
#entity_def["version"] = 1
#entity_def["typeVersion"] = "1.0"


entity_defs.append(entity_def)

entity_def1 = {}
entity_def1["name"] = "azure_cosmosdb_database"
entity_def1["description"] = "azure_cosmosdb_database"
entity_def1["superTypes"] = ["Asset"]
entity_def1["subTypes"] = []
entity_def1["attributeDefs"] = []
entity_def1["attributeDefs"].append({"name":"resourceLink","typeName":"string","isOptional":False,"cardinality": atlas_enumdefs.Cardinality.SINGLE.name,  "valuesMinCount": 1, "valuesMaxCount": 1,"isUnique": False, "isIndexable": False, "includeInNotification": False})
entity_def1["attributeDefs"].append({"name":"ods_zone","typeName":"string","isOptional":False,"cardinality": atlas_enumdefs.Cardinality.SINGLE.name,  "valuesMinCount": 1, "valuesMaxCount": 1,"isUnique": False, "isIndexable": False, "includeInNotification": False})
entity_def1["attributeDefs"].append({"name":"lastModifiedTime","typeName":"date","isOptional":False,"cardinality": atlas_enumdefs.Cardinality.SINGLE.name,  "valuesMinCount": 1, "valuesMaxCount": 1,"isUnique": False, "isIndexable": False, "includeInNotification": False})
entity_def1["attributeDefs"].append({"name":"string","typeName":"string","isOptional":False,"cardinality": atlas_enumdefs.Cardinality.SINGLE.name,  "valuesMinCount": 1, "valuesMaxCount": 1,"isUnique": False, "isIndexable": False, "includeInNotification": False})

entity_defs.append(entity_def1)

print(json.dumps(entity_defs))
### Testing relationships


inp_relationships = []
inp_relationship = {}
inp_relationship["name"] = "cosmosdb_account_database"
inp_relationship["description"] = "cosmosdb_account_database"
inp_relationship["propagateTags"] = atlas_enumdefs.relationship_propagateTags.NONE.name
inp_relationship["relationshipCategory"] = atlas_enumdefs.relationship_category.COMPOSITION.name
 


end1Def = {}
end1Def["name"] = "databases"
end1Def["type"] = "azure_cosmosdb_account"
end1Def["isContainer"] = True
end1Def["cardinality"] = atlas_enumdefs.Cardinality.SINGLE.name
end1Def["isLegacyAttribute"] = False
inp_relationship["endDef1"] = end1Def
end2Def = {}
end2Def["name"] = "account"
end2Def["type"] = "azure_cosmosdb_database"
end2Def["isContainer"] = False
end2Def["cardinality"] = atlas_enumdefs.Cardinality.SINGLE.name
end2Def["isLegacyAttribute"] = False
 
inp_relationship["endDef2"] = end2Def
inp_relationship["relationshipLabel"] = "r:cosmosdb_account_database"
inp_relationships.append(inp_relationship)


### sample input of enums
enum_defs = []
enum_def = {}
enum_def["name"] = "blob_access_tier"
enum_def["elementDefs"] = []
enum_def["elementDefs"].append({"value":"Unknown","ordinal":0,"description":"Unknown access tier"})
enum_def["elementDefs"].append({"value":"Hot","ordinal":1,"description":"Hot access tier"})
enum_def["elementDefs"].append({"value":"Cool","ordinal":2,"description":"Cool access tier"})
enum_def["elementDefs"].append({"value":"Archive","ordinal":3,"description":"Archive access tier"})

enum_defs.append(enum_def)

structDefs_list = []
structDefs = {}
structDefs["category"] = atlas_enumdefs.Category.STRUCT.name
structDefs["name"] = "blob_soft_deleted_state"
structDefs["attributeDefs"] = []
structDefs["attributeDefs"].append({"name":"deleted","typeName":"boolean","isOptional":True,"isIndexable":False,"includeInNotification":False,"cardinality": atlas_enumdefs.Cardinality.SINGLE.name})
structDefs["attributeDefs"].append({"name":"deletedTime","typeName":"date","isOptional":True,"isIndexable":False,"includeInNotification":False,"cardinality": atlas_enumdefs.Cardinality.SINGLE.name})
structDefs["attributeDefs"].append({"name":"deleted","typeName":"boolean","isOptional":True,"isIndexable":False,"includeInNotification":False,"cardinality": atlas_enumdefs.Cardinality.SINGLE.name})
structDefs_list.append(structDefs)

inp_classifications = []
classification = {}
classification["name"] = "GOVERNMENT.CZECH.NATIONAL_ID_CARD_NUMBER"
classification["description"] = "Czech National Identity Card Number"
classification["superTypes"] = []
classification["entityTypes"] = []
classification["subTypes"] = []

inp_classifications.append(classification)

typedefs = {}
typedefs["entityDefs"] = create_typedefs_entities.create_entity_defs(entity_defs)
typedefs["relationshipDefs"] = create_typedefs_relationships.create_relationship_defs(inp_relationships)
typedefs["enumDefs"] = create_typedefs_enum.create_enum_defs(enum_defs)
typedefs["structDefs"] = create_typedefs_structs.create_struct_defs(structDefs_list)
typedefs["classificationDefs"] = create_typedefs_classifications.create_classification_defs(inp_classifications)

print(json.dumps(typedefs))





''' Response for entityDefs and enumDefs
{
    "enumDefs": [
        {
            "category": "ENUM",
            "guid": "99e34c8b-22d5-44f0-9691-da731a2b3744",
            "createdBy": "admin",
            "updatedBy": "admin",
            "createTime": 1570986984,
            "updateTime": 1570986984,
            "version": 1,
            "name": "blob_access_tier",
            "description": "blob_access_tier",
            "typeVersion": "1.0",
            "elementDefs": [
                {
                    "value": "Unknown",
                    "description": "Unknown access tier",
                    "ordinal": 0
                },
                {
                    "value": "Hot",
                    "description": "Hot access tier",
                    "ordinal": 1
                },
                {
                    "value": "Cool",
                    "description": "Cool access tier",
                    "ordinal": 2
                },
                {
                    "value": "Archive",
                    "description": "Archive access tier",
                    "ordinal": 3
                }
            ]
        }
    ],
    "structDefs": [],
    "classificationDefs": [],
    "entityDefs": [
        {
            "category": "ENTITY",
            "guid": "679c65f1-da33-488a-b15d-153ffe70ae15",
            "createdBy": "admin",
            "updatedBy": "admin",
            "createTime": 1570987771539,
            "updateTime": 1570987771539,
            "version": 1,
            "name": "azure_cosmosdb_account",
            "description": "azure_cosmosdb_account",
            "typeVersion": "1.0",
            "attributeDefs": [
                {
                    "name": "api_type",
                    "typeName": "string",
                    "isOptional": false,
                    "cardinality": "SINGLE",
                    "valuesMinCount": 1,
                    "valuesMaxCount": 1,
                    "isUnique": false,
                    "isIndexable": false,
                    "includeInNotification": false
                },
                {
                    "name": "ods_zone",
                    "typeName": "string",
                    "isOptional": false,
                    "cardinality": "SINGLE",
                    "valuesMinCount": 1,
                    "valuesMaxCount": 1,
                    "isUnique": false,
                    "isIndexable": false,
                    "includeInNotification": false
                }
            ],
            "superTypes": [],
            "subTypes": []
        },
        {
            "category": "ENTITY",
            "guid": "23c392df-031e-4cb6-9412-e2425f9dbcac",
            "createdBy": "admin",
            "updatedBy": "admin",
            "createTime": 1570987771544,
            "updateTime": 1570987771544,
            "version": 1,
            "name": "azure_cosmosdb_database",
            "description": "azure_cosmosdb_database",
            "typeVersion": "1.0",
            "attributeDefs": [
                {
                    "name": "resourceLink",
                    "typeName": "string",
                    "isOptional": false,
                    "cardinality": "SINGLE",
                    "valuesMinCount": 1,
                    "valuesMaxCount": 1,
                    "isUnique": false,
                    "isIndexable": false,
                    "includeInNotification": false
                },
                {
                    "name": "ods_zone",
                    "typeName": "string",
                    "isOptional": false,
                    "cardinality": "SINGLE",
                    "valuesMinCount": 1,
                    "valuesMaxCount": 1,
                    "isUnique": false,
                    "isIndexable": false,
                    "includeInNotification": false
                },
                {
                    "name": "lastModifiedTime",
                    "typeName": "date",
                    "isOptional": false,
                    "cardinality": "SINGLE",
                    "valuesMinCount": 1,
                    "valuesMaxCount": 1,
                    "isUnique": false,
                    "isIndexable": false,
                    "includeInNotification": false
                },
                {
                    "name": "string",
                    "typeName": "string",
                    "isOptional": false,
                    "cardinality": "SINGLE",
                    "valuesMinCount": 1,
                    "valuesMaxCount": 1,
                    "isUnique": false,
                    "isIndexable": false,
                    "includeInNotification": false
                }
            ],
            "superTypes": [
                "Asset"
            ],
            "subTypes": []
        }
    ],
    "relationshipDefs": []
}

{
    "enumDefs": [],
    "structDefs": [],
    "classificationDefs": [],
    "entityDefs": [],
    "relationshipDefs": [
        {
            "category": "RELATIONSHIP",
            "guid": "3de748df-f73d-43e7-8d50-0331f17d9457",
            "createdBy": "admin",
            "updatedBy": "admin",
            "createTime": 1570986984,
            "updateTime": 1570986984,
            "version": 1,
            "name": "cosmosdb_account_database",
            "description": "cosmosdb_account_database",
            "typeVersion": "1.0",
            "attributeDefs": [],
            "relationshipCategory": "COMPOSITION",
            "propagateTags": "NONE",
            "endDef1": {
                "type": "azure_cosmosdb_account",
                "name": "databases",
                "isContainer": true,
                "cardinality": "SINGLE",
                "isLegacyAttribute": false
            },
            "endDef2": {
                "type": "azure_cosmosdb_database",
                "name": "account",
                "isContainer": false,
                "cardinality": "SINGLE",
                "isLegacyAttribute": false
            },
            "relationshipLabel": "r:cosmosdb_account_database"
        }
    ]
}


{
    "enumDefs": [],
    "structDefs": [
        {
            "category": "STRUCT",
            "guid": "af02eb07-02e7-4399-9f59-e9dce1851dc6",
            "createdBy": "admin",
            "updatedBy": "admin",
            "createTime": 1571055763,
            "updateTime": 1571055763,
            "version": 1,
            "name": "blob_soft_deleted_state",
            "description": "blob_soft_deleted_state",
            "typeVersion": "1.0",
            "attributeDefs": [
                {
                    "name": "deletedTime",
                    "typeName": "date",
                    "isOptional": true,
                    "cardinality": "SINGLE",
                    "valuesMinCount": 0,
                    "valuesMaxCount": 1,
                    "isUnique": false,
                    "isIndexable": false,
                    "includeInNotification": false
                },
                {
                    "name": "deleted",
                    "typeName": "boolean",
                    "isOptional": true,
                    "cardinality": "SINGLE",
                    "valuesMinCount": 0,
                    "valuesMaxCount": 1,
                    "isUnique": false,
                    "isIndexable": false,
                    "includeInNotification": false
                }
            ]
        }
    ],
    "classificationDefs": [],
    "entityDefs": [],
    "relationshipDefs": []
}

{
    "enumDefs": [],
    "structDefs": [],
    "classificationDefs": [
        {
            "category": "CLASSIFICATION",
            "guid": "bfc94a8a-6016-48bc-93a9-7fe63deb2046",
            "createdBy": "admin",
            "updatedBy": "admin",
            "createTime": 1571059518339,
            "updateTime": 1571059518339,
            "version": 1,
            "name": "GOVERNMENT.CZECH.NATIONAL_ID_CARD_NUMBER",
            "description": "Czech National Identity Card Number",
            "typeVersion": "1.0",
            "attributeDefs": [],
            "superTypes": [],
            "entityTypes": [],
            "subTypes": []
        }
    ],
    "entityDefs": [],
    "relationshipDefs": []
}

{
    "mutatedEntities": {
        "CREATE": [
            {
                "typeName": "azure_cosmosdb_account",
                "guid": "5932beae-352d-414d-b09f-7e522a4d6456",
                "status": "ACTIVE"
            },
            {
                "typeName": "azure_cosmosdb_database",
                "attributes": {
                    "qualifiedName": "testdb"
                },
                "guid": "e6e61138-acd9-48c4-bcb3-28696bfb5adc",
                "status": "ACTIVE"
            }
        ]
    },
    "guidAssignments": {
        "-127818879948768": "e6e61138-acd9-48c4-bcb3-28696bfb5adc",
        "-127818879948767": "5932beae-352d-414d-b09f-7e522a4d6456"
    }
}
'''