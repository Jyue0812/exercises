import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 10

    FLASK_MAIL_SERVER = 'smtp.qq.com'
    FLASK_MAIL_PORT= 465
    FLASK_MAIL_USE_SSL = True
    FLASK_MAIL_USE_TLS = False
    FLASK_MAIL_USERNAME = '1678033705@qq.com'
    FLASK_MAIL_PASSWORD = 'coohdgjzpxsnebab'

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