#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : order.py
# Time       : 2023/3/5 17:17
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：工单管理
"""
import json
import random
from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"    # 显示所有
        # fields = []   # 自定义显示
        exclude = ['oid', 'admin']   # 排除显示哪个


def order_list(request):
    """工单列表"""
    queryset = models.Order.objects.all().order_by('-id')   # 倒序

    page_object = Pagination(request, queryset)
    form = OrderModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        'page_string': page_object.html(),
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """ 新建订单（Ajax请求） """
    form = OrderModelForm(data=request.POST)

    if form.is_valid():
        # 订单号：额外增加一些不是用户输入的值（自己计算出来）
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        # 固定设置管理员ID,去哪里获取？

        form.instance.admin_id = request.session["info"]['id']

        # 保存到数据库中
        form.save()
        # return HttpResponse(json.dumps({"status": True}))
        return JsonResponse({"status": True})

    return JsonResponse({"status": False, 'error': form.errors})


def order_delete(request):
    """ 删除订单 """
    uid = request.GET.get('uid')
    # 判断数据是否存在
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': '删除失败,您要删除的数据不存在'})

    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_detail(request):
    """ 根据ID获取订单详情 """
    # 方法1
    """uid = request.GET.get('uid')
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, 'error': '数据不存在。'})

    # 从数据库中获取一个对象
    result = {
        "status": True,
        "data": {
            'name': row_object.name,
            'price': row_object.price,
            'status': row_object.status,
        }
    }
    return JsonResponse(result)"""

    # 方法2
    uid = request.GET.get('uid')
    # 得到一个字典{"name": Dior, "price": 1564, "status": 2}
    row_dict = models.Order.objects.filter(id=uid).values("name", "price", "status").first()
    # 得到一个字典列表 [{"name": Dior, "price": 1564, "status": 2}, {"name": Dior, "price": 1564, "status": 2}]
    # queryset = models.Order.objects.all().values("name", "price", "status")
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在。"})

    # 从数据库中获取一个对象
    """ {name: "不锈钢保温杯", price: 34, status: 2} """
    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    """ 编辑订单 """
    uid = request.GET.get('uid')
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在"})

    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

