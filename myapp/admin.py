from django.contrib import admin
from myapp.models import Dept,EMP
# Register your models here.
class DeptAdmin(admin.ModelAdmin):
    list_display=['id','dname','location']
    
class EMPAdmin(admin.ModelAdmin):
    list_display=['id','ename','email','phone','sal','deptno']

admin.site.register(Dept,DeptAdmin)
admin.site.register(EMP,EMPAdmin)