from tornado.options import define, options, parse_command_line
from tornado.web import RequestHandler
from tornado.web import template, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

define("port", default=8080, help="port---")
define("debug", default=False, help="debug--")

class BaseHandler(RequestHandler):

    def send_success(self, **kwargs):
        obj = {
            "success": True
        }
        for k in kwargs:
            obj[k] = kwargs[k]
        self.write(obj)

    def send_fail(self, error_text=""):
        obj = {
            "success": False,
            "error_text": error_text
        }
        self.write(obj)

class MainHandler(BaseHandler):
    def get(self):
        return self.render("./templates/index.html")


if __name__ == '__main__':
    parse_command_line()
    app = Application([
        (r"/index", MainHandler),
    ], debug=options.debug)
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.instance().start()