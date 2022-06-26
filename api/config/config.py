import os
from dotenv import load_dotenv
from pathlib import Path

basedir = Path(__file__).parent.parent
load_dotenv()

class LocalConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(basedir, "images.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INCLUDED_EXTENTION = [".png", ".jpg"]
    DIR_NAME = "handwriting_pics"

class DevConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(basedir, "images.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INCLUDED_EXTENTION = [".png", ".jpg"]
    BUCKET = os.environ.get("BUCKET_NAME")
    REGION = os.environ.get("AWS_DEFAULT_REGION")
    FOLDER = os.environ.get("FOLDER_NAME")
