from flask import Blueprint, render_template
from flask_login import login_required

mains = Blueprint('main', __name__)


@mains.route('/')
def index():
    return render_template('common/base.html')


@mains.route('/secret/')
@login_required
def secret():
    return '只有登录用户可访问'