from django.db import models

# Create your models here.

 

class InstiModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    mobileNo = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    colgStu = models.CharField(max_length=200)
    exam=models.CharField(max_length=200)
    feedback = models.CharField(max_length=500)



    def __str__(self):
        return (
            f"{self.name} | "
            f"{self.email} "
        )