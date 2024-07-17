from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar_no=models.IntegerField(unique=True)
    def __str__(self):
        return str(self.aadhar_no)
    
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_age=models.IntegerField(max_length=50)
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.PROTECT)
    def __str__(self):
        return self.stu_name

