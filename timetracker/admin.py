from django.contrib import admin

# Register your models here.
from .models import TimeSheet, Project, Employee

admin.site.register(TimeSheet)
admin.site.register(Project)
admin.site.register(Employee)