import tornado.web
from tornado.options import define, options, parse_command_line
from tornado.web import Application

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello2")

class HelloHandler(tornado.web.RequestHandler):

    # 入口
    # 用于初始化handler类（类实例化方法）
    def initialize(self, db):
        self.db = db

    # 用于真正执行请求方法之前的初始化方法，所有逻辑处理之前都会经过的方法
    def prepare(self):
        # 如打印日志，打开数据库连接
        pass

    # 与prepare方法相反，在执行请求方法结束的时候要执行的方法
    def on_finish(self):
        # 关闭句柄，清理内存，关闭socket
        pass

    # http方法：get， post， delete， patch， put
    # 输入： 一些参数
    def get(self, *args, **kwargs):
        self.get_query_argument("name")
        self.get_query_arguments()


url = [
    (r"/hello", MainHandler)
]

# define 定义一些可以在命令行中传递的参数以及类型
# options是一个类，全局只有一个options,

define("port", default=5555, help="run on the given port", type=int)
define("debug", default=False, help="debug mode", type=bool)

options.parse_command_line()  # 获取命令行传递过来的参数
options.parse_config_file("settings.py")  # 从文件获取

if __name__ == '__main__':
    app = Application(url, debug=options.debug)
    # app.listen(8888)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()