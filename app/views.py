from django.shortcuts import render, redirect, get_object_or_404
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Client



def home(request):
    return render(request, 'home.html')



def register(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Username = request.POST['Username']
        Email = request.POST['Email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']
        if Password1 == Password2:
            if Client.objects.filter(Username=Username).exists():
                messages.error(request, 'Username taken')
                return redirect('register')
            elif Client.objects.filter(Email=Email).exists():
                messages.error(request, 'Email exist')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=First_name, last_name=Last_name, username= Username, password=Password1)
                user.save()
                messages.info(request,'user created')
                return redirect('login')

        else:
            messages.error( request, "Password don't match.")
            return redirect('register')
    else:
        return render(request, 'register.html')


def Login(request):
    if request.method=='POST':
        Username = request.POST['Username']
        Password1 = request.POST['Password1']
        user = auth.authenticate(username=Username,password=Password1)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid LogIn')
            return redirect('login')

    else:

        return render(request, 'Login.html')

@login_required(login_url='register.html')
def Farm(request):
    return render(request, 'farm.html')

def Availability(request):
    return render(request, 'available.html')

def Department(request):
    return render(request, 'department.html')


def Cultivation(request):
    return render(request, 'cultivation.html')

def Treatment(request):
    return render(request, 'treatment.html')


def ContactUs(request):
    return render(request, 'contactUs.html')

def AboutUs(request):
    return render(request, 'aboutUs.html')

