#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Equipment(models.Model):
    typecode = models.CharField(u'型号', max_length=100, primary_key=True)
    Equipment = models.CharField(u'设备', max_length=200)
    brand = models.CharField(u'品牌', max_length=100)
    project = models.CharField(u'使用项目', max_length=200)
    classtype = models.CharField(u'类别', max_length=100)
    price = models.FloatField(u'价格')
    
    class Meta:
        db_table = u"Equipment"
        verbose_name_plural = u'设备表'


