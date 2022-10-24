from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Client(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Username = models.CharField(max_length=200)
    Email = models.CharField(max_length=20, default=True)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

    def __str__(self):
        return self.Username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author= models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title



class Treatment(models.Model):
    phone_no = models.CharField(max_length=10)
    disease_image = models.ImageField(upload_to = 'media/')
    Description = models.TextField(max_length=200)

    def __str__(self):
        return self.phone_no


class Farmer(models.Model):
    Username = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=12)
    Email = models.EmailField(max_length=50)
    Farmer_Image = models.ImageField(upload_to = 'media/farmers')

    def __str__(self):
        return self.Username, phone_no

class Products(models.Model):
    LOCATIONS = (('Budalangi','Budalangi'),('Bulemia','Bulemia'),('Port_victoria','PortVictoria'),('Busia','Busia'),('Igigo','Igigo'),('Sirimba','Sirimba'),)
    Username = models.CharField(max_length=30)
    phone_no = models.IntegerField()
    Product_name = models.CharField(max_length=50)
    Product_Image = models.ImageField(upload_to = 'media/products')
    location = models.CharField(max_length=20, choices=LOCATIONS, default='Budalangi')
    
    def __str__(self):
        return self.Username

# rice
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     types = models.CharField(max_length=50)
#     total = models.IntegerField()
#     immersiveDate = models.DateField(auto_now_add=True, null=True)
#     HarvestDate = models.CharField(max_length=18, null=True)
#     image = models.ImageField(null=True, blank=True)

#     def __str__(self):
#         return self.name


