from azure.core.exceptions import ResourceNotFoundError,HttpResponseError
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient

try:
    def upload_blob_to_folder(connection_string, container_name,local_file_path, blob_name):
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        
        container_client = blob_service_client.get_container_client(container_name)
        
    # Concatenate the folder name with the blob name to form the final blob path
        blob_path =  blob_name
        # print(blob_path)
        blob_client = container_client.get_blob_client(blob_path)
        # print(blob_client)
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data)
            print("done!!!!!!!!")
        
    # Example usage:

    connection_string = "DefaultEndpointsProtocol=https;AccountName=techpathwebsite;AccountKey=bUVR8fgoXk3565ALq06F+yK9ObXM0V6iEA7GqSz6FkcNw1YiFT9MRY1/Ztas5YooWF2EaJ+/vn5l+ASt6rM91A==;EndpointSuffix=core.windows.net"
    container_name = "website"
    local_file_path = "C:/Users/Ranjana/OneDrive - Techpath Research and Development PVT/Pictures/Screenshot_4.png"
    blob_name = "Screenshot_4.png"
    upload_blob_to_folder(connection_string, container_name,local_file_path, blob_name)
    print(f"file '{blob_name}'------------->>> upload successfully")
    
except Exception as e:
    print(repr(e))