from flask import Flask
from app.config import config
from extensions import config_extensions
from app.views import register_blueprint

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name or 'default'))
    config_extensions(app)
    register_blueprint(app)
    return app
