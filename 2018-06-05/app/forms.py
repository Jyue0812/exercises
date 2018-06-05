from flask_wtf import form, FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired, Length(3, 12, '用户名必须在3到12个字符之间')])
    password = StringField('密码', validators=[DataRequired, Length(3, 12, '密码必须在3到12个字符之间'), ])
    password2 = StringField('确认密码', validators=[DataRequired, Length(3, 12, '密码必须在3到12个字符之间'), EqualTo(password)])
    email = StringField(Email())
    submit = SubmitField()