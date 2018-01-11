#-*-coding:utf-8-*-
import tornado.web
import MySQLdb


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')

    def post(self):
        pass