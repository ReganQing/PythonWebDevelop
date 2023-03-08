#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : mobileNumber.py
# Time       : 2023/2/28 13:53
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：靓号管理
"""

from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import NumAddModelForm, NumEditModelForm

# Create your views here.


def num_list(request):
    """靓号列表"""

    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['mobile__contains'] = search_data

    queryset = models.GoodNumber.objects.filter(**data_dict).order_by('-level')

    page_object = Pagination(request, queryset)
    context = {
        "num_info": page_object.page_queryset,      # 分完页的数据
        "page_string": page_object.html(),  # 页码
        "search_data": search_data
    }

    return render(request, "num_list.html", context)

# --------------------------------------------------


def num_add(request):
    """靓号添加"""
    if request.method == "GET":
        form = NumAddModelForm()
        return render(request, "num_add.html", {'form': form})

    # 当用户发出POST请求时，提交修改数据并进行校验
    form = NumAddModelForm(data=request.POST)
    if form.is_valid():
        # 将数据保存到靓号列表
        form.save()
        return redirect('/num/list/')

    # 若校验失败，在页面上显示错误信息
    return render(request, 'num_add.html', {'form': form})

# --------------------------------------------------


def num_edit(request, nid):
    """靓号编辑"""
    row_object = models.GoodNumber.objects.filter(id=nid).first()

    if request.method == "GET":
        # 按照ID索引数据库获取要编辑的那行数据
        form = NumEditModelForm(instance=row_object)
        return render(request, "num_edit.html", {'form': form})

    form = NumEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 将数据保存到靓号列表
        form.save()
        return redirect('/num/list/')

    # 若校验失败，在页面上显示错误信息
    return render(request, 'num_add.html', {'form': form})


def num_del(request, nid):
    """靓号删除"""
    models.GoodNumber.objects.filter(id=nid).delete()
    return redirect("/num/list/")
