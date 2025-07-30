from scripts.s3_uploader import upload_file
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data" / "dirty_data.csv"

if __name__ == '__main__':
    upload_file(data_path)
