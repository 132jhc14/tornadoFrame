from tornado.web import RequestHandler

from runSevers import manager
import json

class BaseHandler(RequestHandler):

    # "first--设置headers"
    def initialize(self) -> None:
        self.manager = manager

    # second--初始化
    def set_default_headers(self) -> None:
        # 处理跨域请求
        print("setting headers!!!")
        self.set_header('Access-Control-Allow-Origin', '*')
        # self.set_header('Access-Control-Allow-Origin', 'http://localhost:8080')
        # self.set_header('Access-Control-Allow-Headers', 'X-Requested-With')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS')
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type')

    def prepare(self):
        print("third--准备工作")
        # if self.request.method in ["POST", "PUT", "DELETE"]:
        #     try:
        #         body = json.loads(self.request.body)
        #         self.request.body = body
        #         print(json.dumps(body))
        #     except:
        #         pass

    # def write_error(self, status_code, **kwargs):
    #     print("fifth--处理错误")
    #
    # def on_finish(self):
    #     print("sixth--处理结束,释放资源--")

