import functools
import jwt
from runSevers.config import jwt_setting, settings, default
from common.utils.message import to_dict_msg
from apps.users.models import Users


def login_require_async(view_func):
    @functools.wraps(view_func)
    async def require(self, *arg, **kwargs):
        # 验证用户是否登录
        # 获取token值
        token = self.request.headers.get('token')
        # 解析token
        paylod = jwt.decode(token, jwt_setting['key'], [jwt_setting['algorithm']], options={'verify_exp': True}, leeway=3600 * 24 * 7)
        if paylod:
        # 通过email查询数据
            uuid = paylod.get('uuid')
            # 有数据，将数据返回
            try:
                if default["mysql"]:
                    user = await self.manager.get(Users, uuid=uuid)
                    self._uuid = user.uuid
                    self._username = user.usernmae
                else:
                    self._uuid = "001"
                    self._username = "admin"
                try:
                    await view_func(self, *arg, **kwargs)
                except:
                    self.finish(to_dict_msg(500, msg='视图函数异常'))
            except:
                self.finish(to_dict_msg(401, msg='请登录后重试'))
        else:
            self.finish(to_dict_msg(401, msg='请登录后重试'))
    return require
