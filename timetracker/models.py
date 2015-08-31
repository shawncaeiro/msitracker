from django.db import models
import datetime

# Create your models here.
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__( self ):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    coreid = models.CharField(max_length=100, default = None)
    department = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project)

    def __unicode__( self ):
        return self.coreid

class TimeSheet(models.Model):
    employee = models.ForeignKey(Employee, default = None, null=True)
    project = models.ForeignKey(Project, default = None, null=True)
    date = models.DateField(default = datetime.date.today, null=True)
    hours = models.IntegerField(default = 0, null=True)

    def __unicode__( self ):
        return "{0} {1} {2}".format( self.employee, self.project, self.date)