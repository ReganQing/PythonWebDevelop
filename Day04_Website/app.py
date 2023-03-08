#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : app.py
# Time       : 2023/2/23 14:14
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：
"""

from flask import Flask, render_template, request
import pymysql
from pymysql import cursors

app = Flask(__name__)


@app.route("/add/user", methods=["GET", "POST"])
def add_usr():
    if request.method == "GET":
        return render_template("add_user.html")

    usrname = request.form.get("user")
    passsword = request.form.get("pwd")
    mobile = request.form.get("mobile")

    # 1.连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd='123456', charset='utf8', db='ron01')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 2.执行SQL，添加数据
    sql = "insert into inf2(usrname,password,mobile) values(%s, %s, %s)"
    cursor.execute(sql, [usrname, passsword, mobile])
    conn.commit()
    # 3.关闭连接
    cursor.close()
    conn.close()

    return '添加成功'


@app.route("/show/user")
def show_user():
    # 1.连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd='123456', charset='utf8', db='ron01')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 2.执行SQL，添加数据
    sql = "select * from inf2"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    print(data_list)
    # 3.关闭连接
    cursor.close()
    conn.close()

    return render_template('show_user.html', data_list=data_list)


if __name__ == '__main__':
    app.run()
