import boto3
from botocore.client import Config
import argparse
import os
from dotenv import load_dotenv

# Load environment variables (first from .env.local, then from .env)
load_dotenv(".env.local")

# Get credentials from environment variables
api_url = os.getenv("API_URL")
bucket = os.getenv("BUCKET")
access_key = os.getenv("ACCESS_KEY")
secret = os.getenv("SECRET")




def count_objects_in_bucket(api_url, bucket, access_key, secret):
    # Create an S3 client
    s3 = boto3.client(
        's3',
        endpoint_url=api_url,  # Custom S3-compatible storage URL
        aws_access_key_id=access_key,
        aws_secret_access_key=secret,
        config=Config(signature_version='s3v4')
    )
    
    object_count = 0
    
    # List objects in the bucket
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket):
        if 'Contents' in page:
            object_count += len(page['Contents'])
    
    return object_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to count the number of objects in an S3-compatible bucket.",
        epilog="If arguments are not provided, default values in the script will be used."
    )
    parser.add_argument("-b", "--bucket", help="Name of the bucket (default: defined in script)")
    parser.add_argument("-a", "--api-url", help="S3-compatible object storage URL (default: defined in script)")
    parser.add_argument("-k", "--key", help="Access key for authentication (default: defined in script)")
    parser.add_argument("-s", "--secret", help="Secret key for authentication (default: defined in script)")
    
    args = parser.parse_args()
    
    # Override defaults with command-line arguments if provided
    bucket = args.bucket if args.bucket else bucket
    api_url = args.api_url if args.api_url else api_url
    access_key = args.key if args.key else access_key
    secret = args.secret if args.secret else secret
    
    object_count = count_objects_in_bucket(api_url, bucket, access_key, secret)
    print(f"Number of objects in bucket '{bucket}': {object_count}")

