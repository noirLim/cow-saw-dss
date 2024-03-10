from io import BytesIO
from django.shortcuts import render,redirect,get_object_or_404
from .forms import HasilForm
from .models import Hasil,Detail_Hasil
from nilai.models import Parameter,Nilai
from kriteria.models import KriteriaSapi,Kriteria
from .utils import *
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa

import pandas as pd

# Create your views here.
def index_hasil(request):
    form = HasilForm()
    context = {"form":form}
    return render(request,"hasil/input_hasil.html",context)

def submit_hasil(request):
    form = HasilForm()
    context = {"form":form}

    data_kriteria_sapi = list(KriteriaSapi.objects.select_related('sapi','kriteria').values(
        "id","nilai",
        'sapi_id','kriteria_id','kriteria__nama_kriteria','sapi__id','sapi__nama_sapi'
    ).order_by('id'))
    data_nilai = list(Nilai.objects.values("id","status","bobot"))
    data_kriteria = list(Kriteria.objects.values("id","nama_kriteria","bobot_kriteria","atribut"))
    data_parameter = list(Parameter.objects.select_related('kriteria','nilai').values(
        "id",
        "nama",
        "min",
        "max",
        "kriteria__id",
        "kriteria__nama_kriteria",
        "kriteria__bobot_kriteria",
        "nilai__id"
    ))

    if request.method == "POST":
        form = HasilForm(request.POST)
        if form.is_valid():
            matrix_keputusan = get_parameter_by_id(data_kriteria_sapi,data_parameter)
            normalisasi = normalisasi_count(matrix_keputusan,data_kriteria,data_nilai)
            hasil_akhir = get_ranking(normalisasi,data_kriteria)
            hasil = form.save()
            
            # simpan ke dalam detail hasil
            saved_hasil =  get_object_or_404(Hasil, id=hasil.id)
            det_hasil = [
                Detail_Hasil(hasil=saved_hasil,nilai_norm=akhir["nilai"],sapi_id=akhir["sapi_id"])
                for akhir in hasil_akhir
            ]
            Detail_Hasil.objects.bulk_create(det_hasil)
            return redirect('/')
        else:
            form = HasilForm()

    return render(request,"hasil/input_hasil.html",context)

def get_all_hasil(request):
    data = Hasil.objects.all()
    custom_labels = {
        'nama':'nama',
        'email':'email',
        'tgl_pemilihan':'Tanggal Pemilihan'
    }

    return render(request,"hasil/daftar.html",{"data":data,"custom_labels":custom_labels})

# download hasil dalam pdf
def get_detail_hasil(request,item_id,tipe):
    data_detail = list(Detail_Hasil.objects.filter(hasil_id=item_id).select_related('sapi').values(
        'id',
        'nilai_norm',
        'sapi__id',
        'sapi__nama_sapi'
    ))
    akhir = sorted(data_detail, key=lambda x: x["nilai_norm"], reverse=True)
    custom_labels = {
        'ranking':"Ranking",
        'nama_sapi':"Nama Sapi",
        'nilai':"Nilai"
    }

    template_path = 'hasil/report.html'  # Assuming your template is named 'download.html'
    context = {
        'custom_labels': custom_labels,  # Replace with your custom labels
        'data': akhir,  # Replace with your data
    }

    if tipe == "pdf":
        html_content = render_to_string(template_path, context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output_sapi.pdf"'
        pisa_status = pisa.CreatePDF(html_content, dest=response)

        # response mengembalikan file pdf
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html_content + '</pre>', content_type='text/html')
        return response
    
    elif tipe == 'excel':
        html_data = create_html_excel(context)

        df_list = pd.read_html(html_data)
        df = df_list[0]

        # Create a BytesIO buffer for the Excel file
        excel_buffer = BytesIO()

        # Save DataFrame to Excel buffer
        df.to_excel(excel_buffer, index=False)

        # Set response headers for Excel file download
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=output.xlsx'

        # Write Excel buffer to the response
        excel_buffer.seek(0)
        response.write(excel_buffer.read())

        return response

    


