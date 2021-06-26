from django.db import models

# Create your models here.

class Dept(models.Model):
    dname = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    def __str__(self):
        return self.dname
    
class EMP(models.Model):
    ename = models.CharField(max_length=30)
    phone = models.IntegerField(unique=True)
    sal = models.FloatField()
    email=models.EmailField(max_length=30,unique=True)
    deptno =models.ForeignKey(Dept, on_delete=models.CASCADE)
    def __str__(self):
        return self.ename
    
