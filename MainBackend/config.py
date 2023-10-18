from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
