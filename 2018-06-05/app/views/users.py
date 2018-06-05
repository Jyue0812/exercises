from flask import Blueprint, render_template
from app.forms import RegisterForm

user = Blueprint('user', __name__)

@user.route('/')
def index():
    return 'user page'

@user.route('/register')
def register():
    form = RegisterForm()
    return render_template('users/register.html', form=form)

@user.route('/login')
def login():
    return '登录'