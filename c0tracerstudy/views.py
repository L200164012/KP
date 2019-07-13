

from django.shortcuts import render
from .models import *
from django.db import models
from django.db.models import *

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
	data1 = MencariPekerjaan.objects.values('nim','f401','f402','f403','f404','f405','f406','f407','f408','f409','f410','f411','f412','f413','f414','f415')
	A = MencariPekerjaan.objects.filter(f401__contains=1).count()
	B = MencariPekerjaan.objects.filter(f402__contains=1).count()
	C = MencariPekerjaan.objects.filter(f403__contains=1).count()
	D = MencariPekerjaan.objects.filter(f404__contains=1).count()
	E = MencariPekerjaan.objects.filter(f405__contains=1).count()
	F = MencariPekerjaan.objects.filter(f406__contains=1).count()
	G = MencariPekerjaan.objects.filter(f407__contains=1).count()
	H = MencariPekerjaan.objects.filter(f408__contains=1).count()
	I = MencariPekerjaan.objects.filter(f409__contains=1).count()
	J = MencariPekerjaan.objects.filter(f410__contains=1).count()
	K = MencariPekerjaan.objects.filter(f411__contains=1).count()
	L = MencariPekerjaan.objects.filter(f412__contains=1).count()
	M = MencariPekerjaan.objects.filter(f413__contains=1).count()
	N = MencariPekerjaan.objects.filter(f414__contains=1).count()
	O = MencariPekerjaan.objects.filter(f415__contains=1).count()
	P = MencariPekerjaan.objects.filter(f401__contains=0).filter(f402__contains=0).filter(f403__contains=0).filter(f404__contains=0).filter(f405__contains=0).filter(f406__contains=0).filter(f407__contains=0).filter(f408__contains=0).filter(f409__contains=0).filter(f410__contains=0).filter(f411__contains=0).filter(f412__contains=0).filter(f413__contains=0).filter(f414__contains=0).filter(f415__contains=0).count()
	context = {"A":A,"B":B,"C":C,"D":D,"E":E,"F":F,"G":G,"H":H,"I":I,"J":J,"K":K,"L":L,"M":M,"N":N,"O":O,"P":P,"data":data1}
	return render(request,"graph2.html",context)


def view_graph3(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph3.html",context)

def view_graph4(request,*args, **kwargs):
	data1 = MencariPekerjaan.objects.values('nim','f6')
	A = MencariPekerjaan.objects.filter(f6__contains=1).count()
	B = MencariPekerjaan.objects.filter(f6__contains=2).count()
	C = MencariPekerjaan.objects.filter(f6__contains=3).count()
	D = MencariPekerjaan.objects.filter(f6__contains=4).count()
	E = MencariPekerjaan.objects.filter(f6__contains=0).count()
	context = {"A":A,"B":B,"C":C,"D":D,"E":E,"data":data1}
	return render(request,"graph4.html",context)

def view_graph5(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph5.html",context)

def view_graph6(request,*args, **kwargs):
	data1 = PekerjaanSekarang.objects.values('nim','f111')
	A = PekerjaanSekarang.objects.filter(f111__contains=1).count()
	B = PekerjaanSekarang.objects.filter(f111__contains=2).count()
	C = PekerjaanSekarang.objects.filter(f111__contains=3).count()
	D = PekerjaanSekarang.objects.filter(f111__contains=4).count()
	E = PekerjaanSekarang.objects.filter(f111__contains=5).count()
	F = PekerjaanSekarang.objects.filter(f111__contains=0).count()
	context = {"A":A,"B":B,"C":C,"D":D, "E":E, "F":F, "data":data1}
	return render(request,"graph6.html",context)

def view_graph7(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph7.html",context)

def view_graph8(request,*args, **kwargs):
	data1 = PekerjaanSekarang.objects.values('nim','f14')
	A = PekerjaanSekarang.objects.filter(f14__contains=1).count()
	B = PekerjaanSekarang.objects.filter(f14__contains=2).count()
	C = PekerjaanSekarang.objects.filter(f14__contains=3).count()
	D = PekerjaanSekarang.objects.filter(f14__contains=4).count()
	E = PekerjaanSekarang.objects.filter(f14__contains=5).count()
	F = PekerjaanSekarang.objects.filter(f14__contains=0).count()
	context = {"A":A,"B":B,"C":C,"D":D, "E":E,'F':F,'data':data1}
	return render(request,"graph8.html",context)

def view_graph9(request,*args, **kwargs):
	test = Admin.objects.using('c0tracerstudy').all()
	context = {"test":len(test)}
	return render(request,"graph9.html",context)

def view_graph10(request,*args, **kwargs):
	data1 = PekerjaanSekarang.objects.values('nim','f161','f162','f163','f164','f165','f166','f167','f168','f169','f1610','f1611','f1612','f1613','f1614')
	# data2 = 
	A = PekerjaanSekarang.objects.filter(f161__contains=1).count()
	B = PekerjaanSekarang.objects.filter(f162__contains=1).count()
	C = PekerjaanSekarang.objects.filter(f163__contains=1).count()
	D = PekerjaanSekarang.objects.filter(f164__contains=1).count()
	E = PekerjaanSekarang.objects.filter(f165__contains=1).count()
	F = PekerjaanSekarang.objects.filter(f166__contains=1).count()
	G = PekerjaanSekarang.objects.filter(f167__contains=1).count()
	H = PekerjaanSekarang.objects.filter(f168__contains=1).count()
	I = PekerjaanSekarang.objects.filter(f169__contains=1).count()
	J = PekerjaanSekarang.objects.filter(f1610__contains=1).count()
	K = PekerjaanSekarang.objects.filter(f1611__contains=1).count()
	L = PekerjaanSekarang.objects.filter(f1612__contains=1).count()
	M = PekerjaanSekarang.objects.filter(f1613__contains=1).count()
	N = PekerjaanSekarang.objects.filter(f161__contains=0,f162__contains=0,f163__contains=0,f164__contains=0,f165__contains=0,f166__contains=0,f167__contains=0,f168__contains=0,f169__contains=0,f1610__contains=0,f1611__contains=0,f1612__contains=0,f1613__contains=0,).count()

	context = {"A":A,"B":B,"C":C,"D":D,"E":E,"F":F,"G":G,"H":H,"I":I,"J":J,"K":K,"L":L,"M":M,"N":N, "data":data1}
	return render(request,"graph10.html",context)

def view_graph11(request,*args, **kwargs):
    test = Profil.objects.all()
    f1 = PekerjaanSekarang.objects.filter(f13=1).count()
    f2 = PekerjaanSekarang.objects.filter(f13=2).count()
    f3 = PekerjaanSekarang.objects.filter(f13=3).count()
    f4 = PekerjaanSekarang.objects.filter(f13=4).count()
    f5 = PekerjaanSekarang.objects.filter(f13=5).count()
    f6 = PekerjaanSekarang.objects.filter(f13=6).count()
    # test = [entry for entry in test]
    # print(test)
    context = {"pendapatan": [f1,f2,f3,f4,f5,f6],"data":test}
    return render(request,"graph11.html",context)