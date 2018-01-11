#-*-coding:utf-8-*-
import tornado.web
from utils.mysqlhelper import get_res


class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        name = self.get_argument('name', None)
        print name
        self.redirect('/index')