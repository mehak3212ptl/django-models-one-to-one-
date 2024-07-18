from django.db import models

# Create your models here.
class car(models.Model):
    car_name=models.CharField(max_length=50)
    def __str__(self):
        return self.car_name
    
class Customer(models.Model):
    customer=models.CharField(max_length=50)
    ages=models.IntegerField()
    car_name=models.ManyToManyField(car)
    def __str__(self):
        return self.customer



