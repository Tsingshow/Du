#-*-coding:utf-8-*-
import tornado.web
import MySQLdb


class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        pass