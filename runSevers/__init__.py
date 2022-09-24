from tornado.web import Application
from runSevers.config import settings, mysql_setting, INSTALLED_APPS, default
import tornado.web

if default['mysql']:
    import peewee_async
    import peewee_async

    database = peewee_async.MySQLDatabase(**mysql_setting)
    manager = peewee_async.Manager(database)
else:
    database = None
    manager = None


def make_app():
    from runSevers.urls import handler
    handler.extend(import_urls())
    app = tornado.web.Application(handler, **settings)
    print("后端服务启动成功，请勿关闭! 测试地址: http://localhost:8888/")
    app.listen(8888)


# 动态导入路由
def import_urls() -> list:
    import importlib
    res = []
    for item in INSTALLED_APPS:
        cls = importlib.import_module(item + ".urls")
        res.extend(cls.urlpatterns)
    return res