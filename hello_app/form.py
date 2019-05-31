from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    openid =StringField('openid',validators=[DataRequired()])       #添加openID的校验器
    remember_me = BooleanField(default=False)