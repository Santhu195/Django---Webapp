from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib.auth.models import User,auth
from .models import cities,rst
from django.middleware import csrf
from .api import get_rest
from django.template import RequestContext
from django.core.paginator import Paginator
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
    c={}
    #c.update(csrf(request))
    if request.user.is_authenticated:
        return redirect('/welcome')
    else:
        c={}
        #c.update(csrf(request))
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
        #rst.objects.all().delete()
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
    rst.objects.all().delete()
    if request.user.is_authenticated:
        city = cities.objects.all()
        data_l= rst.objects.all()
        get_rest(c_id)
        query = request.GET.get("q")
        if query:
            data_l = rst.objects.filter(Q(name__icontains=query)|
            Q(adress__icontains=query))
            rst_name = rst.objects.all()
        paginator = Paginator(data_l,8 ) 

        page = request.GET.get('page')
        data = paginator.get_page(page)

        return render(request, 'details.html',{'city':city,'data':data})
    else:
        messages.info(request, 'Please Login')
        return redirect('/')
