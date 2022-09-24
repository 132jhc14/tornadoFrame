#-*- coding:utf-8 -*-
import asyncio
from tornado.ioloop import IOLoop
from runSevers import make_app


async def main():
    make_app()
    await asyncio.Event().wait()


def start_app():
    make_app()
    # IOLoop.current().start()
    IOLoop.instance().start()


if __name__ == "__main__":
    asyncio.run(main())
    # start_app()

# 打包
# pyinstaller -F -p C:\Users\mayn\Desktop\PyExe\tornadoExe\venv\Scripts -p C:\Users\mayn\Desktop\PyExe\tornadoExe\venv\Lib\site-packages manage.py --additional-hooks-dir=.
