import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a9edf4b2bd26269eb78aa19a5c635626'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_ADDRESS')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')    