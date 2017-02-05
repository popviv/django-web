# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from group.controller.ActionController import *

#from group.lib.Db import Db

#from group.model.Db.Demo import Demo
from group.lib.DbTable import DbTable

def index(request):
	str = "这是demo-index-index方法"

	#config = {"host":"10.70.40.250","root":"root","password":"123456","dbname":"uyagroup_demo"}

	#print config['host']
	#db = Db(config)
	#print __name__
	#db.insert("insert into dl_testdemo(id,count) values(122,2111)")
	#db.insert("insert into dl_testdemo(id,count) values(133,2123)")

	#row = db.getRow("select * from dl_testdemo where id=133")
	#view()
	#demo = Demo()
	#row = demo.getRow("select * from dl_testdemo where id=133")
	#DbTable.Db("Demo")

	#获取一条记录
	row = DbTable.Db("Demo").getRow("select * from dl_testdemo where id=133")
	#print row

	return render(request,'demo/index/index.html',{"str":str,"row":row})


def list(request):
	print __name__
	str = "这是demo-index-list方法"
	return render(request,'demo/index/list.html',{"str":str})


def add(request):
	str = "这是demo-index-add方法"
	return render(request,'demo/index/add.html',{"str":str})

