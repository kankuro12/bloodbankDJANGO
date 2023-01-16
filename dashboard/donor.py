from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from models.models import Donor,BloodRequest

@login_required()
def index(req):
    donors = Donor.objects.all()
    context = {
        "donors": donors
    }
   
    return render(req, 'dashboard/donor/index.html', context)

@login_required()
def bloodRequests(req):
    requests = BloodRequest.objects.all()
    context = {
        "requests": requests
    }
   
    return render(req, 'dashboard/bloodrequests/index.html', context)

