from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=50)
    tugilgan_yil = models.DateField(max_length=50)
    tirik = models.BooleanField(default=True)
    kitoblar_soni = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.ism}, {self.tugilgan_yil}"

class Kitob(models.Model):
    nom = models.CharField(max_length=50)
    janr = models.CharField(max_length=50)
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE)
    sahifa = models.CharField(max_length=50)
    yil = models.DateField()
    def __str__(self):
        return f"{self.nom}, {self.muallif}"

class Student(models.Model):
    ism = models.CharField(max_length=50)
    guruh = models.CharField(max_length=50)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    bitiruvchi = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.ism}, {self.guruh}"

class Record(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob,on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qaytargan_sana = models.DateField()
    def __str__(self):
        return f"{self.student}, {self.kitob}"