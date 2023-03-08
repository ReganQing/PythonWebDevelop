"""Day06 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from app01.views import department, user, mobileNumber, admin, account, task, order, \
    chart, file, bot

urlpatterns = [
    re_path(r"media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}, name='media'),

    # 部门管理
    path("depart/list/", department.depart_list),
    path("depart/add/", department.depart_add),
    path("depart/<int:nid>/del/", department.depart_del),
    path("depart/<int:nid>/edit/", department.depart_edit),  # 利用正则表达式来进行解析
    path("depart/multi/", department.depart_multi),

    # 员工管理
    path("user/list/", user.user_list),
    path("user/model/form/add/", user.user_add_model_form),
    path("user/<int:nid>/edit/", user.user_edit),
    path("user/<int:nid>/del/", user.user_del),

    # 靓号管理
    path("num/list/", mobileNumber.num_list),
    path("num/add/", mobileNumber.num_add),
    path("num/<int:nid>/edit/", mobileNumber.num_edit),
    path("num/<int:nid>/del/", mobileNumber.num_del),

    # 管理员账户
    path("admin/list/", admin.admin_list),
    path("admin/add/", admin.admin_add),
    path("admin/<int:nid>/edit/", admin.admin_edit),
    path("admin/<int:nid>/del/", admin.admin_del),
    path("admin/<int:nid>/reset/", admin.admin_reset),

    # 用户登录
    path("login/", account.login),
    path("logout/", account.logout),
    path("image/code/", account.image_code),
    path("ajax/task/", task.ajax_task),
    # path("ajax/list/", task.ajax_list),
    path("ajax/add/", task.ajax_add),

    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),

    # 上传文件
    path('file/list/', file.upload_file),
    path('upload/form/', file.upload_form),
    path('upload/model/form/', file.upload_model_form),

    # 机器人列表
    path('bot/list/', bot.bot_list),
    path('bot/add/', bot.bot_add),

]
