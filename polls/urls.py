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
    path('login', views.login, name='login'),
    path('user_list/', views.user_list, name='user_list'),
    path('add_user/', views.add_user, name='add_user'),
]