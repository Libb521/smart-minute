import os

class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:1111@localhost/smartminute'
        


class ProdConfig(Config):

 SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class DevConfig(Config):
    DEBUG = True

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")  


config_options = {
'development':DevConfig,
'production':ProdConfig
}