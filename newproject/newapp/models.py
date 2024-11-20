from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USERTYPE=models.CharField(max_length=100)

class Department(models.Model):
    DEPNAME=models.CharField(max_length=100)

class Teacher(models.Model):
    Depid=models.ForeignKey(Department,on_delete=models.CASCADE)
    Tid=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    Address=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)


class Student(models.Model):
    Depid=models.ForeignKey(Department,on_delete=models.CASCADE)
    sid=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    Address=models.CharField(max_length=100)                
    


