#-*- coding:utf-8 -*-
'''
Created on 2014年7月18日

@author: qiaow
'''
from django.contrib import admin
from models import Equipment

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('Equipment', 'typecode', 'brand', 'price','classtype', 'project')
    search_fields = ('Equipment', 'typecode', 'brand')
admin.site.register(Equipment, EquipmentAdmin)