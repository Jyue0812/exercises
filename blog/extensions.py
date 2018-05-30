from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager


db = SQLAlchemy()
boot = Bootstrap()
migrate = Migrate(db=db)
mail = Mail()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def config_extensions(app):
    db.init_app(app)
    boot.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message = '请登录后再访问'