from django.shortcuts import render

# Create your views here.
#coding:utf-8
from django.http import HttpResponse ## http输出类
from django.shortcuts import render
from MyFirstApp.models import * ## 应用所有的数据模型


def index(request):
	return HttpResponse(u"MyFirstApp @ HelloWorld! 上海123") ##字符输出到页面

def add(request,a,b):
    return HttpResponse(str(int(a) + int(b))) ## 将计算结果输出到页面

# default路径的方法
def default(request):
	accountNames = testusers.objects.all() ## 查询testusers表返回所有数据对象
	return render(request, 'default.html', {'accountNames': accountNames}) ## 将查询结果返回到模板页面default.html