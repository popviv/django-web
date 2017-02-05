# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def detail(request):
	str = "这是demo-show-detail方法"
	return render(request,'demo/show/detail.html',{"str":str})
