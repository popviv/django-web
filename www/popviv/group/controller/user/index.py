from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#from group.models import dl_testdemo

from group.model.Db.Demo import Demo

def add(request):
	a = request.GET.get("a",'zhuang')
	b = request.GET.get("b",'qiu min')
	
	list = Demo.objects.all()

	
	response = ""
	for var in list:
		response += "id:"+str(var.id)+"|count:"+str(var.count) + " "


	return HttpResponse("hello world[a:"+a+"][b:"+b+"]["+response+"] --zhuangqm")
