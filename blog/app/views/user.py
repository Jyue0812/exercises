from flask import Blueprint, render_template
from app.forms import RegistrationForm

users = Blueprint('user', __name__)


@users.route('/login/')
def login():
    return render_template('user/login.html')\

@users.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('user/register.html', form=form)