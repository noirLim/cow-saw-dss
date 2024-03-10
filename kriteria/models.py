from django.db import models
from sapi.models import Sapi

# Create your models here.
class Kriteria(models.Model):

    nama_kriteria = models.CharField(max_length=50)
    bobot_kriteria = models.DecimalField(max_digits=5, decimal_places=2)
    satuan = models.CharField(max_length=10)
    atribut = models.CharField(max_length=20)

    # difitur select akan memunculkan nama kriteria tersebut
    def __str__(self):
        return f'{self.nama_kriteria}'

class KriteriaSapi(models.Model):
    nilai = models.FloatField()
    sapi= models.ForeignKey(Sapi,on_delete=models.CASCADE)
    kriteria = models.ForeignKey(Kriteria,on_delete=models.CASCADE)
