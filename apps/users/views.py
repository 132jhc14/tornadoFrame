import asyncio

from common.db.base_handler import BaseHandler
from common.utils.message import to_dict_msg
from apps.users.wtforms import UserForm, LoginUserForm
from apps.users.models import Users
from runSevers.config import jwt_setting, default
import uuid
import jwt


# 用户注册
class UserHandler(BaseHandler):

    async def post(self):
        # 接受请求参数
        user_form = UserForm(self.request.arguments)
        user_code = self.get_body_argument('code')
        if user_code == "0000":
            if user_form.validate():
                # 验证用户是否存在
                phone = user_form.phone.data
                try:
                    exist_user = await self.manager.get(Users, email=phone)
                    if exist_user:
                        self.finish(to_dict_msg(code=500,msg='该手机号码已被注册'))
                except:
                    await self.manager.create(Users, **user_form.data)
                    # 保存数据
                    self.finish(to_dict_msg(code=200,msg='注册成功'))
            else:
                self.finish(to_dict_msg(code=500,msg='注册失败',**user_form.errors))
        else:
            self.finish(to_dict_msg(code=500,msg='验证码错误'))


# 用户登录
class LoginHandler(BaseHandler):

    async def post(self):
        await asyncio.sleep(3)
        user_form = LoginUserForm(self.request.arguments)
        if user_form.validate():
            # 查数据
            try:
                if default["mysql"]:
                    user = await self.manager.get(Users, email=user_form.phone.data, password=user_form.password.data)
                    payload = {
                        'uuid': user.uuid,
                        'username': user.username,
                    }
                else:
                    payload = {
                        'uuid': str(uuid.uuid4()),
                        'username': "admin",
                    }
                token = jwt.encode(payload, **jwt_setting)
                self.finish(to_dict_msg(code=200, msg='登录成功', token=token))
            except Exception as e:
                print(e)
                self.finish(to_dict_msg(code=401, msg='用户名密码错误'))
        else:
            self.finish(to_dict_msg(code=401, msg='用户名密码不合法', **user_form.errors))