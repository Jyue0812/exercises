from .mains import mains
from .users import users

DEFAULT_BLUEPRINT = (
    (mains, ''),
    (users, '/user/')
)


def register_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)