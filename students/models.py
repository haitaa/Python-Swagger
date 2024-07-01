from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    sinif = models.CharField(max_length=10)

    def __str__(self):
      return f"{self.ad} {self.soyad}"
