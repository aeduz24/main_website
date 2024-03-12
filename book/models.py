from django.db import models

# Create your models here.
class BookModel(models.Model):
    date = models.CharField(max_length=100)
    timeslot = models.CharField(max_length=100)  # Assuming timeslot is a text field
    email = models.CharField(max_length=100)
    completed=models.BooleanField(default=False)
    order_id=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email} | {self.date} | {self.timeslot}"