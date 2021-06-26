from django.shortcuts import render
from django.http import HttpResponse
from register.models import *
from django.db.models import Q

# Create your views here.
def student1(request):
    p3=student.objects.exclude(studentid__gte=4)
    return render(request,"student.html",{'res':p3})
    
