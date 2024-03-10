from django import forms
from django.forms import ModelForm
from .models import Sapi

class SapiForm(ModelForm):
    class Meta:
        model = Sapi
        fields = '__all__'
        labels = {
            'kode_sapi': 'Kode',
            'nama_sapi': 'Nama',
            'desc_sapi': 'Deskripsi'
        }

        widgets = {
            'kode_sapi': forms.TextInput(attrs={'class': 'form-control','style':"width:400px",}),
            'nama_sapi': forms.TextInput(attrs={'class': 'form-control','style':"width:400px"}),
            'desc_sapi': forms.Textarea(attrs={'class': 'form-control'}),
        }
