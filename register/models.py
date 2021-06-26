from django.db import models

# Create your models here.
class student(models.Model):
    studentid =models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    email= models.EmailField(max_length=30, unique=True, null=True)
    phone= models.BigIntegerField()
    def __str__(self):
        return self.name