# Generated by Django 2.1 on 2018-08-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyFirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testusers',
            name='createtime',
            field=models.DateTimeField(auto_now=True, verbose_name='账号创建日期'),
        ),
        migrations.AddField(
            model_name='testusers',
            name='idstatus',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='testusers',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='testusers',
            name='accountname',
            field=models.CharField(default='', max_length=20),
        ),
    ]