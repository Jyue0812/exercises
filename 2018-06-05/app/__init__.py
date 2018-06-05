from app.admin import admin as admin_blueprint
from app.admin import admin as home_blueprint
from manage import app

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(home_blueprint, url_prefix='/home')