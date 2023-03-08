#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : bot.py
# Time       : 2023/3/7 23:21
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：机器人列表
"""

from django.shortcuts import render, redirect
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm


class UploadModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.Flowers
        fields = "__all__"


def bot_list(request):
    """机器人列表"""
    queryset = models.Flowers.objects.all()

    return render(request, "bot_list.html", {"queryset": queryset})


def bot_add(request):
    """新建机器人"""
    title = "新建机器人"
    if request.method == "GET":
        form = UploadModelForm()
        return render(request, "upload_model_form.html", {'form': form, "title": title})

    form = UploadModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件会自动保存，并把 字段+上传路径写入到数据库
        form.save()
        return redirect("/bot/list/")
    return render(request, 'upload_model_form.html', {"form": form, 'title': title})
