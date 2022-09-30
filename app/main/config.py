import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_MASK_SWAGGER = False


class DevelopmentConfig(Config):
    # here are variables available only for development environment
    DEBUG = True
    ENV = "Dev"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'database-dev.db')


class ProductionConfig(Config):
    DEBUG = False
    ENV = "Staging"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'database-prod.db')


config_by_name = dict(
    dev=DevelopmentConfig,
    development=DevelopmentConfig,
    prod=ProductionConfig,
    production=ProductionConfig)

key = Config.SECRET_KEY
