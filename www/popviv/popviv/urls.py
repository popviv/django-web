# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

#from django.http import HttpRequest

#print "========url====="

#获取请求的path，不带参数
#request = HttpRequest()
#print type(request)
#print "method-----"+ str(request.method)
#print "path------:"+request.path()      
#获取完整参数         
#print "get_full_path------:"+request.get_full_path()  



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'popviv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','group.views.index'),

    url(r'^add/$','group.views.add',name = "add"),

    url(r'^aa/$','group.views.index',name ="test"),

    url(r'^user/$','group.controller.user.index.add'),
    #url(r'^user/test','group.views.user.test.index'),

    url(r'^demo/$','group.controller.demo.index.index'),
    url(r'^demo/list/$','group.controller.demo.index.list'),
    url(r'^demo/add/$','group.controller.demo.index.add'),

    url(r'^demo/show/$','group.controller.demo.show.detail'),

)
