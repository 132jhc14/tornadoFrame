import peewee
from common.db.base_model import BaseModel


class Users(BaseModel):
    GENDER_KEYS = (
        ("male", "男"),
        ("female", "女"),
    )
    uuid = peewee.CharField(max_length=32, unique=True, verbose_name='用户标识')
    phone = peewee.CharField(max_length=11, verbose_name='手机号码')
    username = peewee.CharField(max_length=32, verbose_name='用户名')
    gender = peewee.CharField(max_length=6, default='male', choices=GENDER_KEYS, verbose_name='性别')
    password = peewee.CharField(max_length=12, verbose_name='用户密码')

    class Meta:
        table_name = '用户信息表'
