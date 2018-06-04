from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[Length(3, 10, '用户名必须在6到10个字符之间')])
    password = PasswordField('密码', validators=[Length(3, 10, '密码必须在6到10个字符之间'), EqualTo('password2', '两次输入的密码不一致，请重新输入')])
    password2 = PasswordField('确认密码', validators=[Length(3, 10, '密码必须在6到10个字符之间')])
    email = StringField('邮箱', validators=[Email(), Length(1, 30, '邮箱必须在1到30个字符之间')])
    submit = SubmitField('立即注册')


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Email(), Length(1, 30, '邮箱必须在1到30个字符之间')])
    password = PasswordField('密码', validators=[Length(3, 10, '密码必须在6到10个字符之间')])
    remember_me = BooleanField('保持登录')
    submit = SubmitField('登录')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')