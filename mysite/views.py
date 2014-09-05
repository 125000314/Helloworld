#-*-encoding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render_to_response
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

def homePage(request):
	return render_to_response("homepage.html")

def hello(request):
	return HttpResponse("hello,Django world")

#bad!!!!
def hello2(request):
	tem = Template("aa11.html")
	con = Context({"username" : "wangqiao"})
	return HttpResponse(tem.render(con))

#good!!
def hello3(request):
	tem = get_template("aa.html")
	con = Context({"username": "wangqiao"})
	return HttpResponse(tem.render(con))
	
def testJQuery(request):
	return render_to_response("testJQuery.html", {"username": "wangqiao4"})
	

def hello5(request):
	username = 'wangqiao5'
	return render_to_response("aa.html", locals())
	
@csrf_exempt
def userInfo(request):
	if request.method =='GET':
		return HttpResponse("please visit this url in 'POST' method")
	
	print 'userinfo () called!!',  request.POST['username'],request.POST['password']
	jsonData = {"username":request.POST['username'].upper(), "password":request.POST['password']}
	return HttpResponse(simplejson.dumps(jsonData,ensure_ascii = False))

def userInfo2(request):
    
    #jsonData = {"username":request.GET['username'].upper(), "password":request.GET['password']}
    print request.GET['usernameall']
    print request.GET['phoneall']
    print request.GET['addressall']
    return HttpResponse("1")
    
def moni(request):
	return render_to_response("moni2.html")

@csrf_exempt 
def login(request):
	if request.method == 'POST':
		print request.POST["username"]
		print request.POST["password"]
		print request.POST["csrfmiddlewaretoken"]
		return render_to_response("aa.html")
	else:
		return render_to_response("login.html", context_instance = RequestContext(request))