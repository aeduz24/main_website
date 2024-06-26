from django.db import models

# Create your models here.

class PaymentModel(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False )

    def __str__(self):
        return (
            f"{self.name} | "
            f"{self.payment_id} "
        )


class InstiModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    mobileNo = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    colgStu = models.CharField(max_length=200)
    exam=models.CharField(max_length=200)
    feedback = models.CharField(max_length=500)
    verified = models.BooleanField(default=False)



    def __str__(self):
        return (
            f"{self.name} | "
            f"{self.email} "
        )
    
class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    mobileNo = models.CharField(max_length=200)

    message = models.CharField(max_length=500)



    def __str__(self):
        return (
            f"{self.name} | "
            f"{self.email} "
        )
    
class MentorReg(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=200)
    coaching = models.CharField(max_length=200)
    year_of_study = models.CharField(max_length=20)  
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.email}"
    
class Mentee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=200)
    coaching = models.CharField(max_length=200)
    year_of_study = models.CharField(max_length=20)  
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.email}"
    