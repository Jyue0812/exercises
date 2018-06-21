from flask import render_template, redirect, url_for, flash
from app.models import User
from werkzeug.security import generate_password_hash
from app.home.forms import RegistForm, UserdetailForm
from . import home
from uuid import uuid4
from app import db


@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/login/")
def login():
    return render_template("home/login.html")


@home.route("/logout/")
def logout():
    return redirect(url_for('home.login'))


@home.route("/regist/", methods=["GET", "POST"])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name = data["name"],
            email = data["email"],
            phone = data["phone"],
            pwd= generate_password_hash(data["pwd"]),
            uuid = uuid4().hex
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功","ok")
    return render_template("home/regist.html", form = form)


@home.route("/user/", methods=["GET", "POST"])
def user():
    form = UserdetailForm()
    if form.validate_on_submit():
        data = form.data
    return render_template("home/user.html", form = form)

@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")


@home.route("/comments/")
def comments():
    return render_template("home/comments.html")

@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")


@home.route("/moviecol/")
def moviecol():
    return render_template("home/moviecol.html")

@home.route("/animation/")
def animation():
    return render_template("home/animation.html")

@home.route("/search/")
def search():
    return render_template("home/search.html")


@home.route("/play/")
def play():
    return render_template("home/play.html")
