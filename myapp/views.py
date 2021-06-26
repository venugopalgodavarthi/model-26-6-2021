from django.shortcuts import render
from myapp.models import * 
from django.db.models import Avg, Max, Min, Count, Sum
# Create your views here.

def sample1(request):   
    #p2=Dept.objects.create(dname="django",location="bang")
    #p2.save()
   # e=EMP.objects.create(ename="rock",phone="996665525",email="rock@gmail.com",sal="75000", deptno_id=2)
    #e.save()
    p3=Dept.objects.all()
    p4=EMP.objects.all().aggregate(Sum('sal'))
    return render(request,"sample.html",{"res":p3,"r":p4})


