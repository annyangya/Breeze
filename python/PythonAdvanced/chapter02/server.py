from tornado import web
import tornado
import time

class MainHandler(web.RequestHandler):

    # 客户端发起不同的请求时，只需要重载不同的请求方法即可
     def get(self, *args, **kwargs):
        self.write("hello world3")

    # async def get(self):
    #     # 使用async会定义成协程
    #     pass

class MainHandler2(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("lallalal")

if __name__ == '__main__':
    app = web.Application(
        [
            ("/", MainHandler),
            ("/he/", MainHandler2),
        ], debug=True
    )
    app.listen(port=5555)
    # 声明， 接口，tornado核心在于ioloop， 所以要声明循环
    tornado.ioloop.IOLoop.current().start()
    """
    在handler 中最好不要写同步的接口，会在一个接口返回之后才返回另一个
    """