from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from models.models import Location

@login_required()
def index(req):
    locations = Location.objects.values()
    context = {
        "locations": locations
    }
    
    print(locations)
    print(context)
    return render(req, 'dashboard/location/index.html', context)
def add(req):
    name=req.POST['name']
    
    location = Location(name=name)
    location.save()
    return redirect('locations')
def edit(req):
    name=req.POST['name']
    id=req.POST['id']
    location = Location.objects.get(id=id)
    location.name=name
    location.save()
    return redirect('locations')