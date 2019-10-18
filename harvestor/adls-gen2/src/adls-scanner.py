# Databricks notebook source
# MAGIC %md
# MAGIC This code block gets environment variables from spark cluster environment variables

# COMMAND ----------

# Get Environment varaibles
import os
KeyVault_Scope = os.environ['Azure_KeyVault_Scope']
KeyVault_ADLSGen2_Access_Secret_Name = os.environ['KeyVault_ADLSGen2_Access_Secret_Name']
ADLSGen2_URL = os.environ['ADLSGen2_URL']
ADLSGen2_FileSystem = os.environ['ADLSGen2_FileSystem']
KeyVault_BlobStorage_Access_Secret_Name = os.environ['KeyVault_BlobStorage_Access_Secret_Name']
BlobStorage_URL = os.environ['BlobStorage_URL']
BlobStorage_Output_Container = os.environ['BlobStorage_Output']
Scan_Depth=os.environ['Scan_Depth']

# COMMAND ----------

# MAGIC %md
# MAGIC set spart configuration to access ADSL Gen 2

# COMMAND ----------


spark.conf.set(
  "fs.azure.account.key."+ADLSGen2_URL,
  dbutils.secrets.get(scope = KeyVault_Scope, key =KeyVault_ADLSGen2_Access_Secret_Name ))

# COMMAND ----------

# MAGIC %md
# MAGIC Set spark config to access Az blob storage account

# COMMAND ----------

# Set spark configuration for output Blob Storage Account
spark.conf.set(
  "fs.azure.account.key."+BlobStorage_URL,
 dbutils.secrets.get(scope = KeyVault_Scope, key = KeyVault_BlobStorage_Access_Secret_Name))

# COMMAND ----------

# MAGIC %md
# MAGIC Function to create a JSON file in Blob storage container

# COMMAND ----------

# Function to create file in output Blob storage account
import time
from datetime import datetime

def uploadtoBlob(content):
  try:
    timenow = datetime.now()
    file_name = str(timenow.strftime("%m%d%Y-%H-%M-%S"))+".json"
    result = dbutils.fs.put("wasbs://"+BlobStorage_Output_Container+"@"+BlobStorage_URL+"/"+file_name,content,True)
    if result == True:
      print("File creation success!")
    else:
      print("File creation failed")
  except Exception as e:
    print('Error occurred while creating blob', e)

# COMMAND ----------

# MAGIC %md
# MAGIC Scanner method

# COMMAND ----------

root_path = "abfss://"+ADLSGen2_FileSystem+"@"+ADLSGen2_URL+"/"

startlevel =1
entitylist=[]
scan_depth= int(Scan_Depth)
def getpath(path, level):
  try:
    for file in dbutils.fs.ls(path):      
      pathvalue = str(file.path)      
      pathvalue_string = pathvalue.split(root_path)      
      pathvalue_entity =pathvalue_string[-1]      
      entitylist.append(pathvalue_entity)
      if level < scan_depth:
        newlevel= level+1        
        getpath(file.path,newlevel)
  except:
    print("Error: Not able to access mount path:"+ path )

# COMMAND ----------

getpath(root_path,startlevel)

# COMMAND ----------

# MAGIC %md
# MAGIC Create entity JSON file

# COMMAND ----------

import json

entity_final=[]
for entity in entitylist:
  entity_json ={
    "entity_type_name": "adls_gen2_resource_set",
    "created_by": "sg",
    "attributes": [{
		"attr_name": "qualifiedName",
		"attr_value": entity,
		"is_entityref": False
     }, 
      {
		"attr_name": "name",
		"attr_value": entity,
		"is_entityref": False
    }
    ]
  }
  entity_final.append(entity_json)
  
json_string= json.dumps(entity_final)
print(json_string)

# COMMAND ----------

# MAGIC %md
# MAGIC Upload generated JSON to Azure Blob Storage

# COMMAND ----------

uploadtoBlob(json_string)
