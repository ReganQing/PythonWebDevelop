#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : SearchData.py
# Time       : 2023/2/23 13:11
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

# 2.发送指令

# cursor.execute("select * from inf2 where id > %s", [2, ])
# data_list = cursor.fetchall()
# for row_dict in data_list:
#     print(row_dict)

# 修改数据
cursor.execute("update inf2 set mobile=%s where id = %s", ["15678452985", 1, ])
conn.commit()


# 3.关闭
cursor.close()
conn.close()
