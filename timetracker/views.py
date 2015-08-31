from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
import datetime
from timetracker.models import TimeSheet, Employee, Project, User
import operator

def history(request):
    d = datetime.date.today()
    e = Employee.objects.get(user = request.user)
    ts = TimeSheet.objects.filter(employee= e).filter(date__lte=d).order_by('-date')
    return render(request, 'history.html', {"ts": ts})

def timeEntry(request):
    e = Employee.objects.get(user = request.user)
    d = datetime.date.today()
    dHistory = {}
    dL = []
    dH = []
    dM = []
    dA = []
    ts = TimeSheet.objects.filter(employee= e).filter(date__lte=d)
    for single_date in (d - datetime.timedelta(n) for n in range(14)):
        if ts.filter(date = single_date).exists():
            sd = ts.get(date= single_date)
            dHistory[single_date] = sd.hours
            dL.append(single_date)
            dH.append(sd.hours)
            dM.append(single_date.strftime('%A'))
            dA.append(single_date.strftime('%Y-%m-%d'))
        else:
            dHistory[single_date] = 0
            dL.append(single_date)
            dH.append(0)
            dM.append(single_date.strftime('%A'))
            dA.append(single_date.strftime('%Y-%m-%d'))
    zX = zip(dL, dH, dM, dA)
    return render(request, 'timeEntry.html', {"ts":ts, "tD": dHistory, "zX": zX})

def profile(request):
    e = Employee.objects.get(user = request.user)
    return render(request, 'profile.html', {"timeS": e})

def index2(request):
    x = request.POST.keys()
    y = request.POST.values()
    u = Employee.objects.get(coreid = request.user.username)
    p = Project.objects.get(name= "testP")
    for d, h in request.POST.iteritems():
        try:
            inDate = datetime.datetime.strptime(d, '%Y-%m-%d')
            obj, created = TimeSheet.objects.get_or_create(employee= u, date=inDate, project=p,
                  defaults={'hours': h})
            if not created:
                obj.hours = h
                obj.save()
        except ValueError:
            pass
    return render(request, 'index2.html', {"timeS": x, "y" : y})

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
