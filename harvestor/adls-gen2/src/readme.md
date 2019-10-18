Scanning ADLS Gen 2 folder strucutre is done using databricks job. 

The python notebook needs the following values in Spark Cluster's environment variables

1. Scan_Depth=<<Scan depth - level to scan - int vale>>
2. BlobStorage_Output=<<Output container name in blob storage>>
3. KeyVault_ADLSGen2_Access_Secret_Name=<<Secret name in KeyVault>>
4. KeyVault_BlobStorage_Access_Secret_Name=<<Secret name in Keyvault for blob storage access key>>
5. BlobStorage_URL=<<URL of the Blob storage [accountname.blob.core.windows.net]>>
6. Azure_KeyVault_Scope=<<Azure KeyVault scope - This scope needs to be managed by Azure Databrics>>
7. ADLSGen2_URL=<<URL of ADLS Gen 2 [accountname.dfs.core.windows.net]>>
8. ADLSGen2_FileSystem=<<Name of the file system to be scanned in ADLS Gen 2>>