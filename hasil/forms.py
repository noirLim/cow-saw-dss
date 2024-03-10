from django import forms
from django.forms import ModelForm
from .models import Hasil,Detail_Hasil

class HasilForm(ModelForm):
    class Meta:
        model = Hasil
        fields = '__all__'

        const_fields = {'class':'form-control','style':"width:400px"}

        widgets = {
            'nama':forms.TextInput(attrs=const_fields),
            'email':forms.EmailInput(attrs=const_fields),
            'tgl_pemilihan':forms.DateInput(attrs={'type': 'date','class':'form-control'})
        }

