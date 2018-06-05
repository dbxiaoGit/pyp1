#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 7:27
# @Author  : x
# @Site    : 
# @File    : urls.py

from django.urls import path

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]