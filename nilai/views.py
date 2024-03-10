from django.shortcuts import render,redirect,get_object_or_404
from .forms import NilaiForm,ParameterForm
from .models import Nilai,Parameter
from django.core.paginator import Paginator,EmptyPage

# Create your views here.
# nilai
def index_nilai(request):
    form = NilaiForm()
    context = {"form":form}
    return render(request,"nilai/input_nilai.html",context)

def submit_nilai_form(request,item_id=None):
    if item_id:
        item = get_object_or_404(Nilai,pk=item_id)
        if request.method == "POST":
            form = NilaiForm(request.POST,instance=item)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = NilaiForm(request.POST,instance=item)
    else:
        if request.method == "POST":
            form = NilaiForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                form = NilaiForm()
    
    return render(request,'base.html')

def get_all_nilai(request):
    data = Nilai.objects.all()
    custom_labels={
        'status':"Status",
        'bobot':"bobot"
    }
    context = {'data':data,'custom_labels':custom_labels}

    return render(request,"nilai/daftar_nilai.html",context)

def get_nilai_by_id(request,item_id):
    item = get_object_or_404(Nilai,pk=item_id)
    form = NilaiForm(instance=item)
    return render(request,"nilai/input_nilai.html",{'item':item,"form":form})

def delete_nilai_by_id(request,item_id):
    item = get_object_or_404(Nilai,pk=item_id)
    item.delete()
    return render(request,'index.html')

# parameter
def index_parameter(request):
    form = ParameterForm()
    context={"form":form}
    return render(request,'nilai/input_parameter.html',context)

# get parameter by id
def get_parameter_by_id(request,item_id):
    item = get_object_or_404(Parameter,pk=item_id)
    form = ParameterForm(instance=item)
    return render(request,"nilai/input_parameter.html",{'item':item,"form":form})

# get all parameter
def get_all_parameter(request):
    data = Parameter.objects.select_related("nilai","kriteria").all()
    data_list = list(
        data.values(
            'id',
            'nama',
            'min',
            'max',
            'nilai__id',
            'nilai__status',
            'kriteria__id',
            'kriteria__nama_kriteria'
        )
    )

    p = Paginator(data_list,5)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    custom_labels = {
        'nama':"Nama",
        'min':"Min",
        'max':"Max",
        'kriteria':"Kriteria",
        'nilai':"Nilai"
    }

    return render(request,"nilai/daftar_parameter.html",{'data':page,'custom_labels':custom_labels})

# submit parameter
def submit_parameter_form(request,item_id=None):
    if item_id:
        item = get_object_or_404(Parameter, pk=item_id)
        if request.method == "POST":
            form = ParameterForm(request.POST,instance=item)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = ParameterForm(instance=item)

    else:
        if request.method == "POST":
            form = ParameterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                form = ParameterForm()
    
    return render(request,'base.html')

# delete parameter
def delete_parameter_by_id(request,item_id):
    item = get_object_or_404(Parameter,pk=item_id)
    item.delete()

    return render(request,'index.html')