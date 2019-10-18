import atlas_enumdefs
import json
'''
1. entityTypes strings[]
2. subTypes string[]
3. superTypes string[] 
4. attributeDefs
5. jsonTypeCategory
4. createTime
5. createdBY
6. dateformatter
7. description
8. guid
9. name
10. options
11. typeersion
12. updateTime
13. updatedBy
14. version
'''
{
            "category": "CLASSIFICATION",
            "guid": "ad9a56a0-efe4-4708-b4a8-1d5179cf13e4",
            "createdBy": "admin",
            "updatedBy": "admin",
            "createTime": 1566356835760,
            "updateTime": 1566356835760,
            "version": 1,
            "name": "GOVERNMENT.CZECH.NATIONAL_ID_CARD_NUMBER",
            "description": "Czech National Identity Card Number",
            "typeVersion": "1.0",
            "attributeDefs": [],
            "superTypes": [],
            "entityTypes": [],
            "subTypes": []
        },



def create_classification_defs(classificationDefs):
    classifications_list = []
    for classificationDef in classificationDefs:
        classification_def = {}
        if classificationDef.get("name") is not None:
            classification_def["name"] = classificationDef["name"]
            classification_def["category"] = atlas_enumdefs.Category.CLASSIFICATION.name
            if classificationDef.get("description") is not None:
                classification_def["description"] = classificationDef["description"]
            else:
                classification_def["description"] = classificationDef["name"]
            if classificationDef.get("superTypes") is not None:
                classification_def["superTypes"] = classificationDef["superTypes"]
            else:
                classification_def["superTypes"] = []
            if classificationDef.get("subTypes") is not None:
                classification_def["subTypes"] = classificationDef["subTypes"]
            else:
                classification_def["subTypes"] = []
            if classificationDef.get("entityTypes") is not None:
                classification_def["entityTypes"] = classificationDef["entityTypes"]
            else:
                classification_def["entityTypes"] = []
            classifications_list.append(classification_def)
    return classifications_list


            
