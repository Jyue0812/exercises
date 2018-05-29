import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FLASK_MAIL_SERVER = 'smtp.qq.com'
    # FLASK_MAIL_PORT = 25
    # FLASK_MAIL_SENDER = 'XXXX@qq.com'
    FLASK_MAIL_USERNAME = 'XXXX@qq.com'
    FLASK_MAIL_PASSWORD = '123456'
    # FLASK_MAIL_SUBJECT_PREFIX = '[flasky]'
    TEMPLATES_AUTO_RELOAD = True

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "blog-dev.sqlite")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "blog-test.sqlite")


class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "blog.sqlite")

config = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'products': ProductConfig,
    'default': DevelopConfig,
}