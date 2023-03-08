"""Day05_Django URL Configuration

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

from django.urls import path
from app01 import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    # www.xxx.com/index/  --> 函数
    path('index/', views.index),

    path('user/list/', views.user_list),

    path('tpl/', views.tpl),

    path('news/', views.news),

    # 用户登录
    path('user/login/', views.login),

    # d对用户数据进行增删改查

    path('user/data/', views.user_data),

    # 添加用户数据
    path('user/add/', views.user_add),

    # 删除用户数据
    path('user/del/', views.user_del),
]
