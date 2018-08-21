from __future__ import unicode_literals
from django.db import models

# Create your models here.

# 生成testusers数据表
class testusers(models.Model):
    accountname = models.CharField(default='', max_length=20)
    password = models.CharField(default='', max_length=20)
    createtime = models.DateTimeField('账号创建日期',auto_now = True)
    idstatus = models.IntegerField(default = 1)