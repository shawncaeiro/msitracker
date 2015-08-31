from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
import datetime
from timetracker.models import TimeSheet, Employee, Project, User
import operator
from django.db.models import Sum



def teamHistory(request):
    e = Employee.objects.get(user = request.user)
    m = e.manages.all()
    ts = TimeSheet.objects.none()
    for sub in m:
        subTS = TimeSheet.objects.filter(employee= sub).exclude(hours = 0)
        ts |= subTS
    ts = ts.order_by('project', '-hours', '-date', 'employee')
    tT = []
    tTotal = ts.order_by().values("employee", "project").annotate(dcount= Sum('hours'))
    for r in tTotal:
        tEmployee = Employee.objects.get(id = r['employee'])
        tProject = Project.objects.get(id = r['project'])
        tT.append((tEmployee, tProject,r['dcount']))
    return render(request, 'teamHistory.html', {"ts": ts, "tTotal": tT})

def history(request):
    d = datetime.date.today()
    e = Employee.objects.get(user = request.user)
    p = e.projects.all()
    if 'pChoice' not in request.POST:
        prjt = p[0] 
    else:
        prjtString = request.POST['pChoice']
        prjt = Project.objects.get(name = prjtString)
    ts = TimeSheet.objects.filter(employee= e).filter(date__lte=d).filter(project = prjt).order_by('-date')
    return render(request, 'history.html', {"ts": ts, "p": p, "prjt": prjt})

def timeEntry(request):
    e = Employee.objects.get(user = request.user)
    p = e.projects.all()
    rP = request.POST.keys()
    rP.append(request.POST.values())
    saveC = ""
    if 'pChoice' not in request.POST:
        prjt = p[0] 
    else:
        prjtString = request.POST['pChoice']
        prjt = Project.objects.get(name = prjtString)
    try:
        prjt = Project.objects.get(name = request.POST['projectSelected'])
    except:
        pass
    if 'enterTime' in request.POST:
        saveC = saveTime(request, prjt)
    d = datetime.date.today()
    dHistory = {}
    dL = []
    dH = []
    dM = []
    dA = []
    ts = TimeSheet.objects.filter(employee= e).filter(date__lte=d).filter(project= prjt)
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
    return render(request, 'timeEntry.html', {"ts":ts, "tD": dHistory, "zX": zX, "p": prjt, "ps": p, "rP" : rP, "saveC" : saveC})

def saveTime(request, prjt):
    x = request.POST.keys()
    y = request.POST.values()
    u = Employee.objects.get(coreid = request.user.username)
    pString = request.POST['projectSelected']
    p = Project.objects.get(name= pString)
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
    return 'Successfully updated timesheet for project {pIn}. Last updated {timeIn}'.format(pIn = pString, timeIn = str(datetime.datetime.now()))

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
