from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment



db = SQLAlchemy()
boot = Bootstrap()
migrate = Migrate(db=db)
mail = Mail()
moment = Moment()

def config_extensions(app):
    db.init_app(app)
    boot.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    moment.init_app(app)