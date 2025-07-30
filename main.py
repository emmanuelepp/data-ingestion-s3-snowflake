from scripts.s3_uploader import upload_file
import os
import sys
from pathlib import Path

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data" / "dirty_data.csv"

if __name__ == '__main__':
    upload_file(data_path)
