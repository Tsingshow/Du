#-*-coding:utf-8-*-
from handlers.login import LoginHandler

url_patterns = [
               (r"/login", LoginHandler),
               (r"/", LoginHandler),
    ]