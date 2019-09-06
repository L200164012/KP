from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.db import models
from django.db.models import *

# Create your views here.
def home_view(request,*args, **kwargs):
    # objs = Profil.objects.using("c0tracerstudy").all();
    # for i in objs:
    #     alm = i.alamat
    #     alm = alm.split("\n")
    #     text = ""
    #     for j in alm:
    #         text = text + j + " "
    #     i.alamat=text
    #     i.save()
    #     print(i.rid)

    # profil = Profil.objects.using('c0tracerstudy').all()
    # th_lulus = []
    # jumlah = []
    # for i in profil:
    #     th_lulus.append(i.th_lulus)
    # th_lulus = list(dict.fromkeys(th_lulus))
    # th_lulus.sort()
    # for o in th_lulus:
    #     x = 0
    #     for i in profil:
    #         if i.th_lulus == o:
    #             x += 1
    #     jumlah.append(x)
    # th_lulus = [list(i) for i in zip(th_lulus, jumlah)]
    # context = {"th_lulus": th_lulus}
    return render(request, "base.html")

def view_graph1(request,*args, **kwargs):
    f3 = MencariPekerjaan.objects.using('c0tracerstudy').values_list("f3",flat=True)
    listF3=[1,2,3,4,5]
    listMencariPekerjaan = []
    for i in listF3:
        listMencariPekerjaan.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f3=i).values_list('nim', flat=True))
    for i in range(len(listMencariPekerjaan)):
        listMencariPekerjaan[i] = len(listMencariPekerjaan[i])
    data = [list(i) for i in zip(listMencariPekerjaan,listF3)]
    context = {"data":data}
    return render(request,"graph1.html",context)

def view_graph2(request,*args, **kwargs):
    listkoldata = ['f401','f402','f163','f403','f405','f406','f407','f408','f409','f410','f411','f412','f413','f414','f415']
    listPekerjaan = []
    for i in listkoldata:
        listPekerjaan.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(i__in=1).values_list('nim', flat=True))
    for i in range(len(listPekerjaan)):
        listPekerjaan[i] = len(listPekerjaan[i])
    data = [list(i) for i in zip(listPekerjaan, listkoldata)]
    context = {"data": data}
    return render(request,"graph2.html",context)

# def view_graph2(request,*args, **kwargs):
# 	data1 = MencariPekerjaan.objects.values('nim','f401','f402','f403','f404','f405','f406','f407','f408','f409','f410','f411','f412','f413','f414','f415')
# 	A = MencariPekerjaan.objects.filter(f401__contains=1).count()
# 	B = MencariPekerjaan.objects.filter(f402__contains=1).count()
# 	C = MencariPekerjaan.objects.filter(f403__contains=1).count()
# 	D = MencariPekerjaan.objects.filter(f404__contains=1).count()
# 	E = MencariPekerjaan.objects.filter(f405__contains=1).count()
# 	F = MencariPekerjaan.objects.filter(f406__contains=1).count()
# 	G = MencariPekerjaan.objects.filter(f407__contains=1).count()
# 	H = MencariPekerjaan.objects.filter(f408__contains=1).count()
# 	I = MencariPekerjaan.objects.filter(f409__contains=1).count()
# 	J = MencariPekerjaan.objects.filter(f410__contains=1).count()
# 	K = MencariPekerjaan.objects.filter(f411__contains=1).count()
# 	L = MencariPekerjaan.objects.filter(f412__contains=1).count()
# 	M = MencariPekerjaan.objects.filter(f413__contains=1).count()
# 	N = MencariPekerjaan.objects.filter(f414__contains=1).count()
# 	O = MencariPekerjaan.objects.filter(f415__contains=1).count()
# 	P = MencariPekerjaan.objects.filter(f401__contains=0).filter(f402__contains=0).filter(f403__contains=0).filter(f404__contains=0).filter(f405__contains=0).filter(f406__contains=0).filter(f407__contains=0).filter(f408__contains=0).filter(f409__contains=0).filter(f410__contains=0).filter(f411__contains=0).filter(f412__contains=0).filter(f413__contains=0).filter(f414__contains=0).filter(f415__contains=0).count()
# 	context = {"A":A,"B":B,"C":C,"D":D,"E":E,"F":F,"G":G,"H":H,"I":I,"J":J,"K":K,"L":L,"M":M,"N":N,"O":O,"P":P,"data":data1}
# 	return render(request,"graph2.html",context)

def view_graph3(request,*args, **kwargs):
    listF5 = [4,5,6,0,1,2,3,7,8]
    listMencariPekerjaan = []
    for i in listF5:
        listMencariPekerjaan.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f5=i).values_list('nim', flat=True))
    for i in range(len(listMencariPekerjaan)):
        listMencariPekerjaan[i] = len(listMencariPekerjaan[i])
    data = [list(i) for i in zip(listMencariPekerjaan, listF5)]
    context = {"data": data}
    return render(request,"graph3.html",context)

def view_graph4(request,*args, **kwargs):
    listF6 = [1,2,3,4]
    listMencariPekerjaan = []
    for i in listF6:
        listMencariPekerjaan.append(
            MencariPekerjaan.objects.using('c0tracerstudy').filter(f6=i).values_list('nim', flat=True))
    for i in range(len(listMencariPekerjaan)):
        listMencariPekerjaan[i] = len(listMencariPekerjaan[i])
    data = [list(i) for i in zip(listMencariPekerjaan, listF6)]
    context = {"data": data}
    return render(request,"graph4.html",context)

def view_graph5(request,*args, **kwargs):
    listF7 = [1,2,3,4]
    listMencariPekerjaan = []
    for i in listF7:
        listMencariPekerjaan.append(
            MencariPekerjaan.objects.using('c0tracerstudy').filter(f7=i).values_list('nim', flat=True))
    for i in range(len(listMencariPekerjaan)):
        listMencariPekerjaan[i] = len(listMencariPekerjaan[i])
    data = [list(i) for i in zip(listMencariPekerjaan, listF7)]
    context = {"data": data}
    return render(request,"graph5.html",context)

def view_graph6(request,*args, **kwargs):
    listF111 = [1,2,3,4,5]
    listPekerjaanSekarang = []
    for i in listF111:
        listPekerjaanSekarang.append(
            PekerjaanSekarang.objects.using('c0tracerstudy').filter(f111=i).values_list('nim', flat=True))
    for i in range(len(listPekerjaanSekarang)):
        listPekerjaanSekarang[i] = len(listPekerjaanSekarang[i])
    data = [list(i) for i in zip(listPekerjaanSekarang, listF111)]
    context = {"data": data}
    return render(request,"graph6.html",context)

def view_graph7(request,*args, **kwargs):
    bidangPekerjaan = BidangPekerjaan.objects.using('c0tracerstudy').values_list("pilihan",flat=True)
    namaBP = []
    for i in bidangPekerjaan:
        namaBP.append(i)
    f12 = PekerjaanSekarang.objects.using('c0tracerstudy').values_list("f12",flat=True)
    listF12 = []
    for i in f12:
        listF12.append(i)
    listF12 = list(dict.fromkeys(f12))
    listF12.sort()
    listPekerjaan = []
    for i in listF12:
        listPekerjaan.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f12=i).values_list('nim', flat=True))
    for i in range(len(listPekerjaan)):
        listPekerjaan[i] = len(listPekerjaan[i])
    data = [list(i) for i in zip(listPekerjaan, listF12)]
    context = {"namaBP":namaBP, "data": data}
    return render(request,"graph7.html",context)

def view_graph8(request,*args, **kwargs):
    listF14 = [1,2,3,4,5]
    listPekerjaanSekarang = []
    for i in listF14:
        listPekerjaanSekarang.append(
            PekerjaanSekarang.objects.using('c0tracerstudy').filter(f14=i).values_list('nim', flat=True))
    for i in range(len(listPekerjaanSekarang)):
        listPekerjaanSekarang[i] = len(listPekerjaanSekarang[i])
    data = [list(i) for i in zip(listPekerjaanSekarang, listF14)]
    context = {"data": data}
    return render(request,"graph8.html",context)

def view_graph9(request,*args, **kwargs):
    listF15 = [1,2,3,4]
    listPekerjaan = []
    for i in listF15:
        listPekerjaan.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f15=i).values_list('nim', flat=True))
    for i in range(len(listPekerjaan)):
        listPekerjaan[i] = len(listPekerjaan[i])
    data = [list(i) for i in zip(listPekerjaan, listF15)]
    context = {"data": data}
    return render(request,"graph9.html",context)

def view_graph10(request,*args, **kwargs):
    listkoldata = [f161,f162,f163,f164,f165,f166,f167,f168,f169,f1610,f1611,f1612,f1613]
    listPekerjaan = []
    for i in listkoldata:
        listPekerjaan.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(i=1).values_list('nim', flat=True))
    for i in range(len(listPekerjaan)):
        listPekerjaan[i] = len(listPekerjaan[i])
    data = [list(i) for i in zip(listPekerjaan, listkoldata)]
    context = {"data": data}
    return render(request,"graph10.html",context)

# def view_graph10(request,*args, **kwargs):
# 	data1 = PekerjaanSekarang.objects.values('nim','f161','f162','f163','f164','f165','f166','f167','f168','f169','f1610','f1611','f1612','f1613','f1614')
# 	# data2 =
# 	A = PekerjaanSekarang.objects.filter(f161__contains=1).count()
# 	B = PekerjaanSekarang.objects.filter(f162__contains=1).count()
# 	C = PekerjaanSekarang.objects.filter(f163__contains=1).count()
# 	D = PekerjaanSekarang.objects.filter(f164__contains=1).count()
# 	E = PekerjaanSekarang.objects.filter(f165__contains=1).count()
# 	F = PekerjaanSekarang.objects.filter(f166__contains=1).count()
# 	G = PekerjaanSekarang.objects.filter(f167__contains=1).count()
# 	H = PekerjaanSekarang.objects.filter(f168__contains=1).count()
# 	I = PekerjaanSekarang.objects.filter(f169__contains=1).count()
# 	J = PekerjaanSekarang.objects.filter(f1610__contains=1).count()
# 	K = PekerjaanSekarang.objects.filter(f1611__contains=1).count()
# 	L = PekerjaanSekarang.objects.filter(f1612__contains=1).count()
# 	M = PekerjaanSekarang.objects.filter(f1613__contains=1).count()
# 	N = PekerjaanSekarang.objects.filter(f161__contains=0,f162__contains=0,f163__contains=0,f164__contains=0,f165__contains=0,f166__contains=0,f167__contains=0,f168__contains=0,f169__contains=0,f1610__contains=0,f1611__contains=0,f1612__contains=0,f1613__contains=0,).count()

# 	context = {"A":A,"B":B,"C":C,"D":D,"E":E,"F":F,"G":G,"H":H,"I":I,"J":J,"K":K,"L":L,"M":M,"N":N, "data":data1}
# 	return render(request,"graph10.html",context)

def view_graph11(request,*args, **kwargs):
    listF13=[1,2,3,4,5,6]
    listPekerjaan = []
    for i in listF13:
        listPekerjaan.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f13=i).values_list('nim', flat=True))
    for i in range(len(listPekerjaan)):
        listPekerjaan[i] = len(listPekerjaan[i])
    data = [list(i) for i in zip(listPekerjaan,listF13)]
    context = {"data":data}
    return render(request,"graph11.html",context)

def fill(request, filter, graph):
    listData=[]
    print(graph)
    listProfil = []
    if request.method == 'POST':
        if graph == 1:
            listData.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f3=filter).values_list('nim', flat=True))
        if graph == 3:
            listData.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f5=filter).values_list('nim', flat=True))
        if graph == 4:
            listData.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f6=filter).values_list('nim', flat=True))
        if graph == 5:
            listData.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f7=filter).values_list('nim', flat=True))
        if graph == 6:
            listData.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f111=filter).values_list('nim', flat=True))
        if graph == 7:
            listData.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f12=filter).values_list('nim', flat=True))
        if graph == 8:
            listData.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f14=filter).values_list('nim', flat=True))
        if graph == 9:
            listData.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f15=filter).values_list('nim', flat=True))
        if graph == 11:
            listData.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f13=filter).values_list('nim', flat=True))
        for i in listData:
            profils = Profil.objects.using('c0tracerstudy').filter(nim__in=i).distinct()
            for profil in profils:
                listProfil.append({
                    'nim':profil.nim,
                    'nama':profil.nama,
                    'th_lulus':profil.th_lulus,
                    'tmp_lhr':profil.tmp_lhr,
                    'tgl_lhr':profil.tgl_lhr,
                    'alamat':profil.alamat
                })
    return JsonResponse(listProfil, safe=False)
