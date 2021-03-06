from django.shortcuts import render, redirect
from MyFirstApp.models import testusers
from django.views.decorators import csrf
from django.core.cache import cache

# 登录页面
def login(request):
    ctx = {}
    try:
        cookie_value = request.COOKIES.get('userinfo')  # 读取cookie
        ctx['rlt'] = cookie_value
        #userinfo = request.session['userinfo']
        key = 'user_session_'+cookie_value
        userinfo = cache.get(key)
        #userinfo = cache.get('user_session_zhenghx')
        ctx['rlt'] += ',' + userinfo
    except:
        ctx['rlt'] = '请登录'
    return render(request, 'login.html', ctx)

# 处理登录请求
def login_go(request):
    request.encoding = 'utf-8'
    ctx = {}
    if request.POST:
        # 有数据
        list = testusers.objects.filter(
            accountname=request.POST['accountName'], password=request.POST['password'])
        if list:
            #request.session['userinfo'] = str(list[0].createtime)
            key = 'user_session_'+str(list[0].accountname)
            cache.set(key, str(list[0].id))
            #cache.set('user_session_zhenghx','helloworld')
            red = redirect('/login/')  # 登录成功，重新定向
            red.set_cookie('userinfo', list[0].accountname)  # 将用户名写入cookie
            return red  # 去重定向页面
        else:
            ctx['rlt'] = '账号和密码错误，请重新登录吧'
            return render(request, 'login.html', ctx)
    else:
        # 无数据
        ctx['rlt'] = '请输入账户和密码'
        return render(request, 'login.html', ctx)
