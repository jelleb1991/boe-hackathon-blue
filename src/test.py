import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Accessing blob data
account_url = "https://hackathlonblob.blob.core.windows.net"
default_credential = DefaultAzureCredential()

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url, credential=default_credential)

local_path = 'data'
local_file_name = 'report'

container_name = 'containertest'

# Create a blob client using the local file name as the name for the blob
container_client = blob_service_client.get_container_client(container= container_name) 

blob_list = container_client.list_blobs()
[x for x in blob_list]


