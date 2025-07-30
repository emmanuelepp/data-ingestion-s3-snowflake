import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno una vez
load_dotenv(dotenv_path=Path(__file__).resolve(
).parents[1] / "config" / "config.env")

# Inicializar S3 una vez
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)


def upload_file(file_path: str):
    bucket = os.getenv("S3_BUCKET_NAME")
    s3_key = os.getenv("S3_FILE_KEY")

    try:
        s3.upload_file(str(file_path), bucket, s3_key)
        print(
            f"File '{file_path}' uploaded correctly to S3 (bucket: {bucket})")
    except Exception as ex:
        print(f"Error uploading the file to S3: {ex}")
