import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY', 'some-really-long-and-unique-string')
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS=False # added just to suppress a warning