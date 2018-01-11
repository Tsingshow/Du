# coding:utf8
import pymysql
from settings import mysql_config as cfg
conn = pymysql.connect(**cfg)
def get_res(sql):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()