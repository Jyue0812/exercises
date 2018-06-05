from flask import Blueprint,render_template

mains = Blueprint('mains', __name__)

@mains.route('/')
def index():
    return render_template('common/index.html')