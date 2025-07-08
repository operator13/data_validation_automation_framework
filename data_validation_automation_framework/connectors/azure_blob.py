from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

class AzureBlobConnector:
    def __init__(self, connection_string, container_name):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def fetch_blob_to_df(self, blob_name, file_type='csv', **kwargs):
        blob_client = self.container_client.get_blob_client(blob_name)
        stream = blob_client.download_blob().readall()
        if file_type == 'csv':
            return pd.read_csv(io.BytesIO(stream), **kwargs)
        elif file_type == 'parquet':
            return pd.read_parquet(io.BytesIO(stream), **kwargs)
        else:
            raise ValueError('Unsupported file type') 