from wtforms_tornado import Form
from wtforms.fields import StringField, HiddenField
from wtforms.validators import DataRequired, Length
from uuid import uuid4


# 用户注册
class UserForm(Form):
    uuid = HiddenField(default=str(uuid4()))
    phone = StringField('电话', validators=[Length(min=11, max=11, message='请输入11位的手机号码')])
    username = StringField('昵称', validators=[Length(min=2, max=10, message='请输入2-10长度的昵称')])
    password = StringField('密码', validators=[Length(min=2, message='请输入密码')])


# 用户登录
class LoginUserForm(Form):
    phone = StringField('账号', validators=[Length(min=11, max=11, message='请输入11位的手机号码')])
    password = StringField('密码', validators=[Length(min=6, max=12, message='请输入密码')])

