from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('farm/', views.Farm, name='farm'),
    path('available/', views.Availability, name='available'),
    path('department/', views.Department, name='department'),
    path('cultivation/', views.Cultivation, name='cultivation'),
    path('treatment/', views.Treatment, name='treatment'),
    path('aboutUs/', views.AboutUs, name='aboutUs'),
    path('contacUs/', views.ContactUs, name='contactUs'),
    path('logout/', views.logout, name='logout'),
    path('farmers/', views.Farmer, name = 'farmers'),
    path('product/', views.Product, name = 'product'),
   
]