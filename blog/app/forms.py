from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, equal_to, required, email


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[required(), length(4, 10, '用户名必须在4到10个字符之间')])
    password = PasswordField('密码', validators=[required(), length(6, 10, '密码必须在6到10个字符之间')])
    password2 = PasswordField('确认密码', validators=[required(), equal_to(password, '两次输入的密码不一致，请重新输入')])
    email = StringField('邮箱', validators=[required(), email(), length(1, 30)])
    submit = SubmitField('立即注册')
