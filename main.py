#-*-coding:utf-8-*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from settings import settings
from urls import url_patterns
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self,url_patterns, **settings):
        tornado.web.Application.__init__(self,url_patterns, **settings)

def make_app():
    return Application(url_patterns, **settings)
    
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()