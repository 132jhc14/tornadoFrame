from common.db.base_handler import BaseHandler


class IndexHandler(BaseHandler):

    async def get(self):
        self.write('已启动后端服务，你可以放心使用!')