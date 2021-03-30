from django.contrib import admin
from .models import Student_Info

class Student_Admin(admin.ModelAdmin):
    list_display = ['roll','name','per']

#to view model in admin Panel we need to register here
admin.site.register(Student_Info,Student_Admin)

