from flask import Blueprint,render_template

article = Blueprint('article', __name__)

@article.route('/')
def arti():
    return render_template('blogs/blog_list.html')