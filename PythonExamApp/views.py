from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index(request):
    return render(request, "MainPage.html")

def register(request):
    print(request.POST)

    ValidationError = User.objects.regValidator(request.POST)
    print("Errors are below.")
    print(ValidationError)

    if len(ValidationError)> 0:
        for key, value in ValidationError.items():
            messages.error(request, value)
        return redirect("/")

    else: 
        newUser = User.objects.create(name = request.POST['name'], username = request.POST['username'], password = request.POST['pass'])

    request.session['loginID'] = newUser.id 

    return redirect("/travels")

def travels(request):
    if 'loginID' not in request.session:
        messages.error(request, "Please log in.")
        return redirect("/")
    
    context ={
        'loginUser': User.objects.get (id= request.session['loginID']),
        'AllItems': item.objects.all(),
        'favitem': item.objects.filter(traveltrips = User.objects.get (id= request.session['loginID'])),
        'nonfavitem': item.objects.exclude(traveltrips = User.objects.get (id= request.session['loginID']))
    }
    return render(request, 'travels.html', context)

def login(request):
    print(request.POST)
    ValidationError = User.objects.loginValidation(request.POST)
    print("Errors are below.")
    print(ValidationError)

    if len(ValidationError)> 0:
        for key, value in ValidationError.items():
            messages.error(request, value)
        return redirect("/")
    else:
        userswithSameusername = User.objects.filter(username = request.POST['username'])
        request.session['loginID'] = userswithSameusername[0].id

    

    return redirect("/travels")

def logout(request):
    request.session.clear()

    return redirect("/")

def travelinfo(request, ItemId):
    context = {
        'itemselected': item.objects.get(id= ItemId),
        'trvlitem': item.objects.filter(traveltrips = User.objects.get(id= request.session['loginID'])),
    }


    return render(request, "travelinfo.html", context)

def addtrip(request):

    return render(request, "addtrip.html")

def uploadtrip(request):
    print(request.POST)
    ValidationError = item.objects.createItemVal(request.POST)
    print(ValidationError)

    if len(ValidationError)> 0:
        for key, value in ValidationError.items():
            messages.error(request, value)
        return redirect("/addtrip")
    else:
        item.objects.create(trip_name = request.POST['destination'], plan = request.POST['desc'], startdate = request.POST['datefrom'], enddate = request.POST['dateto'], creator = User.objects.get (id= request.session['loginID']))

    return redirect("/travels")

def travelInfo(request, ItemId):
    context = {
        'itemselected': item.objects.get(id= ItemId),
        
    }
    return render(request, "travelinfo.html")

def jointrip(request, ItemId):
    item.objects.get(id=ItemId).traveltrips.add(User.objects.get(id=request.session['loginID']))

    return redirect("/travels")

def removetrip(request, ItemId):
    item.objects.get(id=ItemId).traveltrips.remove(User.objects.get(id=request.session['loginID']))

    return redirect("/travels")

def deletetrip(request, ItemId):
    item.objects.get(id=ItemId).delete()
    
    return redirect("/travels")



