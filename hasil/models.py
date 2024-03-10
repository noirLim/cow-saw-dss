from django.db import models
from kriteria.models import Kriteria
from sapi.models import Sapi

# Create your models here.
class Hasil(models.Model):
    nama = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    tgl_pemilihan = models.DateField()

class Detail_Hasil(models.Model):
    nilai_norm = models.FloatField()
    sapi = models.ForeignKey(Sapi,on_delete=models.CASCADE)
    hasil = models.ForeignKey(Hasil,on_delete=models.CASCADE)

    