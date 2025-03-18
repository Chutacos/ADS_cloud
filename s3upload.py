import boto3
import os
import config

s3 = boto3.client(
    's3',
    aws_access_key_id=config.AWS_ACCESS_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY,
    region_name=config.AWS_REGION
)

local_folder = "ADS_cloud"

def upload_files():
    for file_name in os.listdir(local_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(local_folder, file_name)
            
            print(f"Uploading {file_name} to S3...")
            s3.upload_file(file_path, config.S3_BUCKET_NAME, file_name)

    print("All CSV files uploaded successfully!")

upload_files()
