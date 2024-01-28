from django.db import models

class users(models.Model):
    uname=models.CharField(max_length=150)
    uemail=models.CharField(max_length=150)
    upassword=models.CharField(max_length=150)
    uaim=models.CharField(max_length=150)

class udetail(models.Model):
    varr=models.CharField(max_length=150)
    weight=models.FloatField(max_length=20)
    height=models.FloatField(max_length=20)
    age=models.FloatField(max_length=20)
    bmi=models.FloatField(max_length=20)
    status=models.CharField(max_length=150)