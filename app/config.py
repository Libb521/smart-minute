import os

class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:@localhost/smartminute'
        


class ProdConfig(Config):

 SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    DEBUG = True

    


config_options = {
'development':DevConfig,
'production':ProdConfig
}