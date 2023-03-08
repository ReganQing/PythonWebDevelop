from django.shortcuts import render, HttpResponse, redirect
from .models import UserInfo, Department

# Create your views here.


def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # 1.优先去项目根目录的templates去找（提前先配置）
    # 2.去app目录下的templates目录寻找user_list.html（根据app的注册顺序,逐一去他们的templates没目录中去找）
    return render(request, "user_list.html")


def add_user(request):

    return render(request, "add_user.html")


def tpl(request):
    return render(request, "tpl.html")


def news(request):
    # https://movie.douban.com/ithil_j/activity/movie_annual2022?with_widgets=1
    # 向这个网址发起请求
    import requests
    res = requests.get('https://www.autohome.com.cn/aspx/GetDealerInfoByCityId2021.aspx?cityid=310100')
    data_list = res.json()
    print(data_list)
    return render(request, "news.html")


# url="网址" headers={"User-Agent"：浏览器协议}，res=request.get(url=url,headers=headers)

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是POST请求，获取用户提交的数据
    # print(request.POST)
    usrname = request.POST.get("user")
    pwd = request.POST.get("password")

    if usrname == "Ron" and pwd == "123":
        # return HttpResponse("登录成功")
        return redirect("https://movie.douban.com/ithil_j/activity/movie_annual2022?with_widgets=1")

    # return HttpResponse("用户名或密码错误，登录失败")
    return render(request, "login.html", {'error_msg': "用户名或密码错误，登录失败"})


def user_data(request):

    # 1.增添数据
    # UserInfo.objects.create(username="Carl", pwd="123", age=19)
    # UserInfo.objects.create(username="Mogo", pwd="456", age=27)
    # UserInfo.objects.create(username="Sout", pwd="qwer", age=23)
    # UserInfo.objects.create(username="Lisa", pwd="ERV4", age=22)

    # 2. 修改数据
    # UserInfo.objects.filter(id=1).update(username="Mike")
    # UserInfo.objects.all().update(age=20)

    # 3.查看用户数据
    # 获取所有数据
    data_list = UserInfo.objects.all()
    # 渲染，返回给用户
    return render(request, "user_data.html", {'data_list': data_list})


def user_add(request):
    if request.method == "GET":
        return render(request, "user_add.html")

    # 获取用户提交的数据
    usr = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

    # 向数据库添加数据
    UserInfo.objects.create(username=usr, pwd=pwd, age=age)

    return redirect('/user/data/')


def user_del(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()

    return redirect('/user/data/')





