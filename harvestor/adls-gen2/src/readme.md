Scanning ADLS Gen 2 folder strucutre is done using databricks job. 

The python notebook needs the following values in Spark Cluster's environment variables

Scan_Depth=<<Scan depth - level to scan - int vale>>
BlobStorage_Output=<<Output container name in blob storage>>
KeyVault_ADLSGen2_Access_Secret_Name=<<Secret name in KeyVault>>
KeyVault_BlobStorage_Access_Secret_Name=<<Secret name in Keyvault for blob storage access key>>
BlobStorage_URL=<<URL of the Blob storage [accountname.blob.core.windows.net]>>
Azure_KeyVault_Scope=<<Azure KeyVault scope - This scope needs to be managed by Azure Databrics>>
ADLSGen2_URL=<<URL of ADLS Gen 2 [accountname.dfs.core.windows.net]>>
ADLSGen2_FileSystem=<<Name of the file system to be scanned in ADLS Gen 2>>