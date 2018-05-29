from flask_script import Manager, prompt_bool
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
manage = Manager(app)
bootstrap = Bootstrap(app)
#配置链接地址
base_url = os.path.abspath(os.path.dirname(__file__))
database_uri = "sqlite:///" + os.path.join(base_url, "data.sqlite")
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri


db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/')
def create():
    db.create_all()
    return "数据库已创建"

@app.route('/drop/')
def drop():
    db.drop_all()
    return "数据库已删除"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(60), unique=True)
#命令行创建数据库
@manage.command
def createall():
    if prompt_bool("真的要创建吗？"):
        db.create_all()
        return "数据库已创建"
    return "数据库bu已创建"

#插入数据
@app.route('/insert/')
def insert():
    dong = User(username = "dong", email = "dong@163.com")
    db.session.add(dong)
    db.session.commit()

    # 插入多条数据
    # db.session.add_all(dong, xxx, xxx, xxx)
    return "dong"

@app.route('/select/<uid>/')
def select(uid):
    u = User.query.get(uid)
    if u:
        return u.username
    return 'wu'

@app.route('/update/<uid>')
def update(uid):
    u = User.query.get(uid)
    if u:
        u.email = 'xxx@163'
        return 'yigai'
    return 'wu'

#数据自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


#禁止数据追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
if __name__ == '__main__':
    manage.run()