from scripts.s3_uploader import upload_file
from scripts.snowflake_client import get_snowflake_conn
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / "config" / "config.env")

data_path = BASE_DIR / "data" / "dirty_data.csv"

if __name__ == '__main__':
    upload_file(
        data_path,
        bucket=os.getenv("AWS_BUCKET_NAME"),
        s3_key=os.getenv("AWS_S3_KEY")
    )
    get_snowflake_conn()
