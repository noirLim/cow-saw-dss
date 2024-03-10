from django.shortcuts import render,redirect,get_object_or_404
from .forms import SapiForm
from .models import Sapi

# Create your views here.
def index_sapi(request):
    form = SapiForm()
    context = {"form":form}
    return render(request,"sapi/input.html",context)

def get_sapi_by_id(request,item_id):
    item = get_object_or_404(Sapi, pk=item_id)
    form = SapiForm(instance=item)
    return render(request,"sapi/input.html",{"item":item,"form":form})

def get_all_sapi(request):
    data = Sapi.objects.all()
    custom_labels = {
        'kode_sapi': 'Kode',
        'nama_sapi': 'Nama',
        'desc_sapi': 'Deskripsi',
    }
    return render(request,'sapi/daftar.html',{'data':data,'custom_labels':custom_labels})

def submit_sapi_form(request,item_id=None):
    if item_id:
        # Editing an existing item
        item = get_object_or_404(Sapi, pk=item_id)
        if request.method == "POST":
            form = SapiForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = SapiForm(instance=item)
    else:
        # membuat record baru
        if request.method == "POST":
            form = SapiForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = SapiForm()
    
    return render(request, 'base.html')

def delete_sapi_by_id(request,item_id):
     item = get_object_or_404(Sapi, pk=item_id)
     item.delete()

     return render(request, 'index.html')
