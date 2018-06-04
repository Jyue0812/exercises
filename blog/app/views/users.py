from flask import Blueprint, render_template, flash, redirect, request,url_for, abort
from app.forms import RegistrationForm, LoginForm
from app.email import send_mail
from app.models import User
from flask_login import login_user,login_required,logout_user,current_user
from extensions import db
from app.models import Post


users = Blueprint('user', __name__)

@users.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('用户名或密码无效')
    return render_template('user/login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@users.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail('账号激活', form.email.data, 'email/activate.html', user=user, token=token)
        flash('点击链接激活')
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('user/register.html', form=form)


@users.route('/activate/<token>')
@login_required
def activate(token):
    if current_user.confirmed():
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('激活成功')
    else:
        flash('激活失败')
        return redirect(url_for('main.index'))


@login_required
@users.route('/profile/<username>')
def profile(username):
    username = User.query.filter_by(username=username).first()
    if username is None:
        abort(404)
    posts = username.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user/profile.html', username=username, posts=posts)

#修改头像
@login_required
@users.route('/icon/')
def icon():
    return render_template('user/icon.html')



# @users.before_app_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.ping()
#         if not current_user.confirmed \
#                 and request.endpoint[:5] != 'user.':
#             return redirect(url_for('user.unconfirmed'))

#
# @users.route('/unconfirmed/')
# def unconfirmed():
#     if current_user.is_anonymous or current_user.confirmed:
#         return redirect(url_for('main.index'))
#     return render_template('user/unconfirmed.html')