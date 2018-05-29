from flask import Blueprint, render_template

mains = Blueprint('main', __name__)


@mains.route('/')
def index():
    return render_template('common/base.html')