#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : chart.py
# Time       : 2023/3/7 11:30
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：数据统计图表
"""
from django.shortcuts import render
from django.http import JsonResponse
from app01 import models


def chart_list(request):
    """ 数据统计 """

    return render(request, "chart_list.html")


def chart_bar(request):
    """ 构造柱状图的数据 """
    # 可以去数据库中获取的数据
    legend = ['Camel', 'Liam']
    series_list = [
        {'name': 'Camel',
         'type': 'bar',
         'data': [5, 20, 36, 10, 10, 20]
         },
        {
            'name': 'Liam',
            'type': 'bar',
            'data': [8, 15, 40, 41, 2, 13]
        }]
    x_axs = ['1月', '2月', '3月', '4月', '5月', '6月']
    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'x_axs': x_axs
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    """ 构造饼状图的数据 """
    # 可以去数据库中获取的数据
    db_data_list = [
        {"value": 1048, "name": '扫地机器人'},
        {"value": 735, "name": '智能音箱'},
        {"value": 580, "name": '智能管家'},
        {"value": 484, "name": '洗碗机器人'},
        {"value": 300, "name": '厨房机器人'}
    ]

    result = {
        "status": True,
        "data": db_data_list,
    }

    return JsonResponse(result)


def chart_line(request):
    """ 构造折线图的数据 """
    legend = ['扫地机器人', '智能音箱', '智能管家', '洗碗机器人', '厨房机器人']
    series_list = [
        {
            "name": '扫地机器人',
            "type": 'line',
            "stack": 'Total',
            "data": [120, 132, 101, 134, 90, 230, 210]
        },
        {
            "name": '智能音箱',
            "type": 'line',
            "stack": 'Total',
            "data": [220, 182, 191, 234, 290, 330, 310]
        },
        {
            "name": '智能管家',
            "type": 'line',
            "stack": 'Total',
            "data": [150, 232, 201, 154, 190, 330, 410]
        },
        {
            "name": '洗碗机器人',
            "type": 'line',
            "stack": 'Total',
            "data": [320, 332, 301, 334, 390, 330, 320]
        },
        {
            "name": '厨房机器人',
            "type": 'line',
            "stack": 'Total',
            "data": [820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]

    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis
        }

    }

    return JsonResponse(result)
