from django.db import models
from kriteria.models import Kriteria

# Create your models here.
class Nilai(models.Model):
    status = models.CharField(max_length=10)
    bobot = models.IntegerField()

    def __str__(self):
        return f'{self.status}'

class Parameter(models.Model):
    nama = models.CharField(max_length=50)
    min = models.FloatField()
    max = models.FloatField()
    kriteria = models.ForeignKey(Kriteria,on_delete=models.CASCADE)
    nilai = models.ForeignKey(Nilai,on_delete=models.CASCADE)