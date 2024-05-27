# File: config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///exam_office.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    WTF_CSRF_ENABLED = True
