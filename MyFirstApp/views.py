from django.shortcuts import render, redirect
from django.core.cache import cache
from django.http import HttpResponse ## http输出类
from MyFirstApp.models import * ## 应用所有的数据模型


def index(request):
	return HttpResponse(u"MyFirstApp @ HelloWorld! 上海123") ##字符输出到页面

def add(request,a,b):
    return HttpResponse(str(int(a) + int(b))) ## 将计算结果输出到页面

# default路径的方法
def default(request):
	key = testusers.objects.all() ## 查询testusers表返回所有数据对象
	return render(request, 'default.html', {'accountNames': key}) ## 将查询结果返回到模板页面default.html

# 添加1,000,000条数据（测试结果为782秒，每秒1278条）
def logs_add(request):
	i = 0
	while i<1000000:
		logs.objects.create(logscontent='logs'+str(i))
		i+=1
	return HttpResponse(u'写入了'+str(i)+'记录')

def view_logs(request):
	list = logs.objects.all()
	return render(request,'logs.html',{'logs':list})