import imp
from django.http import HttpResponse
from django.shortcuts import render

from DemoApp.models import User

def home(req):
    return render(req, 'index.html', {'id' : ''})

def login(req):
    return render(req, 'login.html', {})

def verify(req):
    print(req.POST)
    users = User.objects.filter(username = req.POST['username'], pwd = req.POST['password'])
    if len(users) > 0:
        return render(req, 'index.html', {'id' : req.POST['username']})

    else:
        return HttpResponse("Invalid user")

def logout(req):
    return render(req, 'index.html', {'id' : ''})