from enum import Enum
import time
import json

#ASSOCIATION, AGGREGATION, COMPOSITION
''' 
1. blockedPropagatedClassifications
    1.1 entityGuid
    1.2 entityStatus [ACTIVE, DELETED]
    1.3 propagateStatus
    1.4 removePropagationsOnEntityDelete
    1.5 validityPeriods
        1.5.1 endTime (string)
        1.5.2 startTime (string)
        1.5.3 timeZone (string)
2. createTime
3. createdBy
4. end1
    4.1 guid
    4.2 typeName
    4.3 uniqueAttributes
5. end2
    5.1 guid
    5.2 typeName
    5.3 uniqueAttributes
6. guid
7. homeId
8. label
9. propagateTags
10. propagatedClassifications []
    10.1 entityGuid
    10.2 entityStatus [ACTIVE, DELETED]
    10.3 propagateStatus
    10.4 removePropagationsOnEntityDelete
    10.5 validityPeriods
        10.5.1 endTime (string)
        10.5.2 startTime (string)
        10.5.3 timeZone (string)
11. status  [ACTIVE, DELETED]
12. updateTime
13. updatedBy
14. version
15. attributes
16. typeName
17. createTime
18. updateTme
19. createdBy
20. updatedBy
21.  name

'''

class relationship_status(Enum):
    ACTIVE = 1
    DELETED = 2
user_name = "admin"

inp_relationships = []
inp_relationship = {}

end1 = {}
end1["guid"] = "e6e61138-acd9-48c4-bcb3-28696bfb5adc"
end1["typeName"] = "azure_cosmosdb_account"
end1["uniqueAttributes"] = {}

inp_relationship["end1"] = end1

end2 = {}
end2["guid"] = "5932beae-352d-414d-b09f-7e522a4d6456"
end2["typeName"] = "azure_cosmosdb_database"
end2["uniqueAttributes"] = {}

inp_relationship["end2"] = end2
inp_relationship["homeId"] = "3de748df-f73d-43e7-8d50-0331f17d9457"
inp_relationship["label"] = "Azure Cosmos DB Account to Azure Cosmos DB Database"
inp_relationship["status"] = relationship_status.ACTIVE.name
inp_relationship["typeName"] = "cosmosdb_account_database"
inp_relationship["name"] = "relationshipbetweencosmosaccountanddb"
inp_relationships.append(inp_relationship)

print(json.dumps(inp_relationships))


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


print(json.dumps(create_relationships_def(inp_relationships)))