#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : connectSQL.py
# Time       : 2023/2/23 11:24
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：
"""

import pymysql
from pymysql import cursors

# 1.连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd='123456', charset='utf8', db='ron01')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令(千万不要用字符串格式化去做SQL的拼接，安全隐患SQL注入)
# sql = "insert into inf2(usrname,password,mobile) values(%s,%s,%s)"
# cursor.execute(sql, ['Iris', '123', '12456664562'])

sql = "insert into inf2(usrname,password,mobile) values(%(n1)s,%(n2)s,%(n3)s)"
cursor.execute(sql, {"n1": 'Alan', "n2": '163', "n3": '13745664562'})

conn.commit()

# 3.关闭
cursor.close()
conn.close()