import boto3
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

BASE_DIR = Path(__file__).resolve().parents[1]


def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )


def upload_file(file_path: Path, bucket: str, s3_key: str):
    s3 = get_s3_client()
    try:
        s3.upload_file(str(file_path), bucket, s3_key)
        logging.info(
            f"File '{file_path}' uploaded correctly to S3 (bucket: {bucket})")
    except Exception as ex:
        logging.error(f"Error uploading the file to S3: {ex}")
