#-*-coding:utf-8-*-
from handlers.login import LoginHandler
from handlers.index import IndexHandler

url_patterns = [
               (r"/login", LoginHandler),
               (r"/", LoginHandler),
               (r"/index", IndexHandler),
    ]