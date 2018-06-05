from .mains import mains
from .articles import article
from .users import user

DEFAULT_BLUEPRINT = (
    (mains, ''),
    (article, '/article/'),
    (user, '/user/'),
)

def register_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)