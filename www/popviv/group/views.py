from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	#return render(request,'index/home.html')
	a = request.GET.get("a",11)
	b = request.GET.get("b",22)
	li = {"test1":['11','22','33','44'],"test2":["55","66","77"]}
	return render(request,'index/home.html',{"a":a,"b":b,"li":li})
	#return HttpResponse("hello world[a:"+a+"][b:"+b+"] --zhuangqm")

def add(request):
	a = request.GET.get("a",'1')
	b = request.GET.get("b",'2')

	return HttpResponse("hello world[a:"+a+"][b:"+b+"] --zhuangqm")

#def test(request):
	#return render(request,'home.html')