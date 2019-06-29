

from django.shortcuts import render
from .models import Admin,Profil

# Create your views here.
def home_view(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"home.html",context)

def view_graph1(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph1.html",context)

def view_graph2(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph2.html",context)

def view_graph3(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph3.html",context)

def view_graph4(request,*args, **kwargs):
	test = Profil.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph4.html",context)

def view_graph5(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph5.html",context)

def view_graph6(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph6.html",context)

def view_graph7(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph7.html",context)

def view_graph8(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph8.html",context)

def view_graph9(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph9.html",context)

def view_graph10(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph10.html",context)

def view_graph11(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph11.html",context)