from django import forms
from django.forms import ModelForm
from .models import Kriteria,KriteriaSapi,Sapi

class KriteriaForm(ModelForm):
    class Meta:
        model = Kriteria
        fields = '__all__'
        
        const_fields = {'class': 'form-control','style':"width:400px"}
        bobot = {'max': 300,'min':0}
        bobot.update(const_fields)

        # TWO_CHOICES =  {
        #     "blue": "Blue",
        #     "green": "Green",
        #     "black": "Black",
        # }

        widgets = {
            'nama_kriteria': forms.TextInput(attrs=const_fields),
            'bobot_kriteria':forms.NumberInput(attrs=bobot),
            'satuan':forms.TextInput(attrs=const_fields),
            # 'atribut': forms.MultipleChoiceField(choices=TWO_CHOICES)
        }

class KriteriaSapiForm(ModelForm):
    class Meta: 
        model = KriteriaSapi
        fields = '__all__'
        const_fields = {'class': 'form-control','style':"width:400px"}

        widgets = {
            'nilai':forms.NumberInput(attrs=const_fields),
            'kriteria':forms.Select(attrs=const_fields),
            'sapi':forms.Select(attrs=const_fields)
        }