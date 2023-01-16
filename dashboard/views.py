from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

@login_required()
def index(req):
    return render(req,'dashboard/index.html')

@login_required()
def signout(req):
    logout(req)
    return redirect('signin')
    
    
def signin(req):
    # raise Exception(req.user.is_authenticated)
    if req.user.is_authenticated:
        return redirect('dashboard')
    else:
        if req.method =='POST':
            username = req.POST['username']
            password = req.POST['password']
            # raise Exception({username,password})
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(req, user)
                return redirect('dashboard')
            else:
                messages.error(req, "Bad Credentials!!")
                return redirect('signin')
                
        else:
            return render(req,'auth/index.html')
        