from django.shortcuts import render,redirect,get_object_or_404
from .forms import KriteriaForm,KriteriaSapiForm
from .models import Kriteria,KriteriaSapi
from django.core.paginator import Paginator,EmptyPage

# Create your views here.
# bagian kriteria
def index_kriteria(request):
    form = KriteriaForm()
    context = {"form":form}
    return render(request,"kriteria/input.html",context)

def get_kriteria_by_id(request,item_id):
    item = get_object_or_404(Kriteria,pk=item_id)
    form = KriteriaForm(instance=item)
    return render(request,"kriteria/input.html",{'item':item,"form":form})

def get_all_kriteria(request):
    data = Kriteria.objects.all()
    custom_labels = {
        'nama_kriteria':"Nama Kriteria",
        'bobot_kriteria':"Bobot Kriteria",
        'satuan': "Satuan",
        'atribut':"Atribut"
    }
    return render(request,"kriteria/daftar.html",{'data':data,'custom_labels':custom_labels})

def submit_kriteria_form(request,item_id=None):
    if item_id:
        item = get_object_or_404(Kriteria, pk=item_id)
        if request.method == "POST":
            form = KriteriaForm(request.POST,instance=item)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = KriteriaForm(instance=item)

    else:
        if request.method == "POST":
            form = KriteriaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                form = KriteriaForm()
    
    return render(request,'base.html')

def delete_kriteria_by_id(request,item_id):
    item = get_object_or_404(Kriteria,pk=item_id)
    item.delete()

    return render(request,'index.html')


# bagian form kriteria-sapi
# input kriteria-sapi
def index_kriteria_sapi(request):
    form = KriteriaSapiForm()
    context = {"form":form}
    return render(request,"kriteria/input_kriteria_sapi.html",context)

# ambil semua data kriteria-sapi
def get_all_kriteria_sapi(request):
    # melakukan join ke table sapi dan kriteria untuk ambil value lain
     # ekuivalen dengan 
    # select s.*,x.*,a.* from kriteria_kriteriasapi s
    # left outer join sapi_sapi x on x.id = s.sapi_id
    # left outer join kriteria_kriteria a on a.id = s.kriteria_id
    data = KriteriaSapi.objects.select_related('sapi', 'kriteria').all()
    data_list = list(
        data.values(
            'id',
            'nilai',
            'sapi__id',
            'sapi__nama_sapi',
            'kriteria__id',
            'kriteria__nama_kriteria'
        )
    )
    
    p = Paginator(data,5)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    custom_labels = {
        'nilai':'Nilai',
        'sapi':"Sapi",
        'kriteria':"Kriteria"
    }
    context = {
        'kriteria_sapi_list': page,
        'custom_labels':custom_labels
    }

    return render(request, 'kriteria/daftar_kriteria_sapi.html', context)

# ambil data kriteria-sapi berdasarkan primary key
def get_kriteria_sapi_by_id(request,item_id):
    item = get_object_or_404(KriteriaSapi.objects.select_related('sapi', 'kriteria'), pk=item_id)
    form = KriteriaSapiForm(instance=item)
    return render(request,"kriteria/input_kriteria_sapi.html",{'item':item,"form":form})

# simpan data kriteria-sapi
def submit_kriteria_sapi_form(request,item_id=None):
    if item_id:
        item = get_object_or_404(KriteriaSapi,pk=item_id)
        if request.method =="POST":
            form = KriteriaSapiForm(request.POST,instance=item)
            if form.is_valid():
                form.save()
                return redirect("/")
        else:
            form = KriteriaSapiForm(instance=item)
    else:
        if request.method == "POST":
            form = KriteriaSapiForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                form = KriteriaSapiForm()
    
    return render(request,"index.html")

def delete_kriteria_sapi_by_id(request,item_id):
    item = get_object_or_404(KriteriaSapi,pk=item_id)
    item.delete()
    
    return render(request,'index.html')



