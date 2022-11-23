from django.db import models

# Create your models here.
class TableMobil(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    nama = models.CharField(max_length=50)
    harga = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nama