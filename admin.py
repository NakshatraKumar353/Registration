from django.contrib import admin
from Regapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['No','Name','Age','Mob','Add']
admin.site.register(Student,StudentAdmin)
