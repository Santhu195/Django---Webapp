from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User,auth
from .models import cities,rst
from .api import get_rest
# Create your views here.

def register(request):
    sys_messages = messages.get_messages(request)
    for message in sys_messages:
        pass
    sys_messages.used = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            print ('takeb')
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            print ('takeb')
            return redirect('/')
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            print("user created successfully please login")
            return redirect('/welcome')
    else:
        pass
    return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/welcome')

        else:
            messages.info(request, 'Username or Password does not match')
            return redirect('/')

    else:
        pass
    return render(request, 'register.html') 

def welcome(request):
    if request.user.is_authenticated:
        rst.objects.all().delete()
        city = cities.objects.all()
        return render(request, 'cities.html',{'city':city})
    else:
        messages.info(request, 'Please Login')
        return redirect('/')

def logouts(request):
    messages.info(request, 'Log Out Successful')
    logout(request)
    return redirect('/')

def details(request, c_id, c_name):
    #rst.objects.all().delete()
    if request.user.is_authenticated:
        city = cities.objects.all()
        data= rst.objects.all()
        get_rest(c_id)
        return render(request, 'details.html',{'city':city,'data':data})
    else:
        messages.info(request, 'Please Login')
        return redirect('/')
    
def sss(request):
    if request.user.is_authenticated:
        return render(request, 'test.html')
    else:
        messages.info(request, 'Please Login')
        return redirect('/')