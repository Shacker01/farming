from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client
from .models import Treatment, Farmer, Products
from .forms import TreatmentForm, FarmerForm, ProductsForm



def splash(request):
    return render(request, 'splash.html')

@login_required(login_url = 'register')
def home(request):
    context = {}
    context['product'] = Products.objects.all()
    return render(request, 'home.html', context)



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



def Farm(request):
    return render(request, 'farm.html')


def Availability(request):
    return render(request, 'available.html')

def Department(request):
    return render(request, 'department.html')


def Cultivation(request):
    return render(request, 'cultivation.html')

def Treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance

        else:
            form = TreatmentForm()
    form = TreatmentForm()            
    return render(request, 'treatment.html', {'form':form})


def ContactUs(request):
    return render(request, 'contactUs.html')

def AboutUs(request):
    return render(request, 'aboutUs.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def Farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance

        else:
            form = FarmerForm()
    form = FarmerForm()            
    return render(request, 'farmers.html', {'form':form})

def Product(request):
    if request.method== 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance
            return redirect("product")

        else:
            form = ProductsForm()
    form = ProductsForm()
    return render(request, 'product.html', {'form':form})

# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'files.html')

# class Product(LoginRequiredMixin,CreateView):
#     model = Product
#     login_url = 'login'
#     form_class = ProductForm
#     template_name = 'app/templates/pro_upload.html'
#     success_url = reverse_lazy('product.html')