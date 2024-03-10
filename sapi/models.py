from django.db import models

# Create your models here.
class Sapi(models.Model):
    kode_sapi = models.CharField(max_length=6,unique=True)
    nama_sapi = models.TextField()
    desc_sapi = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.nama_sapi

