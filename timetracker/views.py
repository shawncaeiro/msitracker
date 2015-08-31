from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
import datetime
from timetracker.models import TimeSheet, Employee, Project, User
import operator

def history(request):
    e = Employee.objects.get(user = request.user)
    ts = TimeSheet.objects.filter(employee= e).filter(date__lte='2015-08-27')
    return render(request, 'history.html', {"ts": ts})

def timeEntry(request):
    e = Employee.objects.get(user = request.user)
    d = datetime.date.today()
    dHistory = {}
    dL = []
    dH = []
    ts = TimeSheet.objects.filter(employee= e).filter(date__lte='2015-08-27')
    for single_date in (d - datetime.timedelta(n) for n in range(14)):
        if ts.filter(date = single_date).exists():
            sd = ts.get(date= single_date)
            dHistory[single_date] = sd.hours
            dL.append(single_date)
            dH.append(sd.hours)
        else:
            dHistory[single_date] = 0
            dL.append(single_date)
            dH.append(0)
    zX = zip(dL, dH)
    return render(request, 'timeEntry.html', {"ts":ts, "tD": dHistory, "zX": zX})

def profile(request):
    e = Employee.objects.get(user = request.user)
    return render(request, 'profile.html', {"timeS": e})

def index(request):
    try:
        e = Employee.objects.get(name = request.user.username)
    except:
        pass

    ts = TimeSheet(
        employee = e,
        project = Project.objects.get(name= "testP"),
        week = 1,
        mon = 2,
        tues = 2,
        wed = 3,
        thurs = 4,
        fri = 5,
        sat = 6,
        sun = 7
        )
    #a = request.POST['Monday']
    a =1
    ts.save()
    return render(request, 'index.html', {"a":a})
