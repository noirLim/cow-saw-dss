from django import forms
from django.forms import ModelForm
from .models import Nilai,Parameter

class NilaiForm(ModelForm):
    class Meta:
        model = Nilai
        fields = '__all__'

        const_fields = {'class': 'form-control','style':"width:400px"}

        widgets = {
              'status': forms.TextInput(attrs=const_fields),
              'bobot':forms.NumberInput(attrs=const_fields),
        }

class ParameterForm(ModelForm):
    class Meta:
        model = Parameter
        fields = '__all__'

        const_fields = {'class': 'form-control','style':"width:400px"}

        widgets = {
            'nama':forms.TextInput(attrs=const_fields),
            'min':forms.NumberInput(attrs=const_fields),
            'max':forms.NumberInput(attrs=const_fields),
            'kriteria':forms.Select(attrs=const_fields),
            'nilai':forms.Select(attrs=const_fields),
        }