from django.db import models

# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=255)
    num_guests=models.IntegerField()
    booking_date=models.DateTimeField()

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2,max_digits=5)
    inventory=models.IntegerField()

    def __str__(self):
        return self.title