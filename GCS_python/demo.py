import os
import pathlib
import mimetypes
from google.cloud import storage #pip install google-cloud-storage
STORAGE_CLASSES = ('STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE')
class GCStorage:
   def __init__(self, storage_client):
       self.client = storage_client
   def create_bucket(self, bucket_name, storage_class, bucket_location='US'):
       bucket = self.client.bucket(bucket_name)
       bucket.storage_class = storage_class
       return self.client.create_bucket(bucket, bucket_location)        
   def get_bucket(self, bucket_name):
       return self.client.get_bucket(bucket_name)
   def list_buckets(self):
       buckets = self.client.list_buckets()
       return [bucket.name for bucket in buckets]
   def upload_file(self, bucket, blob_destination, file_path):
       file_type = file_path.split('.')[-1]
       if file_type == 'csv':
           content_type = 'text/csv'
       elif file_type == 'psd':
           content_type = 'image/vnd.adobe.photoshop'
       else:
           content_type = mimetypes.guess_type(file_path)[0]
       blob = bucket.blob(blob_destination)#blob data type that stores binary data
       blob.upload_from_filename(file_path, content_type=content_type) #upload_from_filename:built in function to upload file
       return blob
   def list_blobs(self, bucket_name):
       return self.client.list_blobs(bucket_name)

# Step 1. prepare the variables
working_dir = pathlib.Path.cwd()#.path generate path
files_folder = working_dir.joinpath('My Files') # joinpath combine paths with eachother
downloads_folder = working_dir.joinpath('Downloaded') 
bucket_name = 'gcs_api_demo_01'

# Step 2. construct GCStorage instance
storage_client = storage.Client()
gcs = GCStorage(storage_client)
# Step 3. Create gcp_api_demo Cloud Storage bucket
if not bucket_name in gcs.list_buckets():
   bucket_gcs = gcs.create_bucket('gcs_api_demo_01', STORAGE_CLASSES[0])
else:
   bucket_gcs = gcs.get_bucket(bucket_name)


# Step 4. Upload Files
for file_path in files_folder.glob('*.*'): #glob provide pattern to match with dir/sub dir
   # use file name without the extension
   gcs.upload_file(bucket_gcs, 'without extension/' + file_path.stem, str(file_path))
   # use full file name
   gcs.upload_file(bucket_gcs, file_path.name, str(file_path))




