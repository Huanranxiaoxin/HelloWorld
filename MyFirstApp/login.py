from django.http import HttpResponse
from django.shortcuts import render,redirect
from MyFirstApp.models import *
from django.views.decorators import csrf
from django.views.decorators.cache import cache_page


# 登录页面
def login(request):
    ctx = {}
    try:
        cookie_value = request.COOKIES.get('userinfo') # 读取cookie
        ctx['rlt'] = cookie_value
    except:
        ctx['rlt'] = '请登录'
    return render(request, 'login.html', ctx)

# 处理登录请求
def login_go(request):
    request.encoding = 'utf-8'
    ctx = {}
    if request.POST:
        # 有数据
        message = request.POST['accountName'] +','+ request.POST['password']
        list = testusers.objects.filter(accountname = request.POST['accountName'], password = request.POST['password'])
        if list:
            red = redirect('/login/') # 登录成功，重新定向
            red.set_cookie('userinfo',list[0].accountname) # 将用户名写入cookie
            return red # 去重定向页面
        else:
            message = '账号和密码错误，请重新登录吧'
    else:
        # 无数据
        message = '请输入账户和密码'
    ctx['rlt'] = message
    return render(request, 'login.html', ctx)