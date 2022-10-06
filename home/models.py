from django.db import models

# Create your models here.
class Department(models.Model):
    depname=models.CharField(max_length=50)
    depdes=models.CharField(max_length=250)

    def __str__(self):
        return self.depname

class Doctor(models.Model):
    dname=models.CharField(max_length=50)
    depname=models.ForeignKey(Department, on_delete=models.CASCADE)
    ddes=models.TextField(max_length=1000)
    dimg=models.ImageField(upload_to="doctorss")
    
    def __str__(self):
        return self.dname
        return self.depname        
        return self.ddes
        return self.dimg


class Booking(models.Model):
    pname=models.CharField(max_length=50)
    pemail=models.EmailField(max_length=254)
    dname=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pdate=models.DateField()
    bdate=models.DateField( auto_now=True)