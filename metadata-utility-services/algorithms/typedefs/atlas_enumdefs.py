## All the default  enums in Atlas

from enum import Enum

class Cardinality(Enum):
    SINGLE = 1
    LIST = 2
    SET = 3


class Category(Enum):
    PRIMITIVE =1 
    OBJECT_ID_TYPE = 2
    ENUM = 3
    STRUCT = 4
    CLASSIFICATION = 5
    ENTITY = 6
    ARRAY = 7
    MAP = 8
    RELATIONSHIP = 9



class relationship_propagateTags(Enum):
     NONE = 1
     ONE_TO_TWO = 2
     TWO_TO_ONE = 3
     BOTH = 4

class relationship_category(Enum):
    ASSOCIATION = 1
    AGGREGATION = 2
    COMPOSITION = 3 