from django.shortcuts import render
from .models import Profil, MencariPekerjaan,BidangPekerjaan,PekerjaanSekarang,Admin
from django.http import JsonResponse
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

    profil = Profil.objects.using('c0tracerstudy').all()
    th_lulus = []
    jumlah = []
    for i in profil:
        th_lulus.append(i.th_lulus)
    th_lulus = list(dict.fromkeys(th_lulus))
    th_lulus.sort()
    for o in th_lulus:
        x = 0
        for i in profil:
            if i.th_lulus == o:
                x += 1
        jumlah.append(x)
    th_lulus = [list(i) for i in zip(th_lulus, jumlah)]
    context = {"th_lulus": th_lulus}
    return render(request, "home.html", context)

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
    test = Admin.objects.using('c0tracerstudy').all()
    context = {"test":len(test)}
    return render(request,"graph2.html",context)

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
    test = Admin.objects.using('c0tracerstudy').all()
    context = {"test":len(test)}
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
    test = Admin.objects.using('c0tracerstudy').all()
    context = {"test":len(test)}
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
    test = Admin.objects.using('c0tracerstudy').all()
    context = {"test":len(test)}
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
    test = Admin.objects.using('c0tracerstudy').all()
    context = {"test":len(test)}
    return render(request,"graph10.html",context)

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
    listProfil = []
    if request.method == 'POST':
        if graph == 1:
            listData.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f3=filter).values_list('nim', flat=True))
        if graph == 3:
            listData.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f5=filter).values_list('nim', flat=True))
        if graph == 5:
            listData.append(MencariPekerjaan.objects.using('c0tracerstudy').filter(f7=filter).values_list('nim', flat=True))
        if graph == 7:
            listData.append(PekerjaanSekarang.objects.using('c0tracerstudy').filter(f12=filter).values_list('nim', flat=True))
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
