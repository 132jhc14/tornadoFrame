import os

SECRET_KEY = 'f6wudg$cwtz$t44kn!w2l_x$z4k=1(4ihg6myvu88m9#@ms)v3'

#
DEBUG = True

# 是否使用数据库
MYSQL = False

base_path = os.path.abspath(os.path.dirname(__file__))

INSTALLED_APPS = [
    'runSevers',
    'apps.users',
]

default = {
    "mysql": MYSQL
}

settings = {
    'static_path': os.path.join(base_path, './static'),
    'static_url_prefix': '/static/',
    'debug': DEBUG,
}

mysql_setting = {
    'database': 'forum',
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'xxx',
}

redis_setting = {
    'host': '192.168.67.128',
    'port': '6379',
}

jwt_setting = {
    'key': SECRET_KEY,
    'algorithm': 'HS256'
}
