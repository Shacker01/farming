from django.contrib import admin
from .models import Client
from .models import Treatment, Farmer, Products

@admin.register(Treatment)
class TreatmentTable(admin.ModelAdmin):
    list_display = ['phone_no', 'Description']

@admin.register(Client)
class ClientTable(admin.ModelAdmin):
    list_display = ['Username']

@admin.register(Farmer)
class FarmerTable(admin.ModelAdmin):
    list_display = ['Username', 'phone_no', 'Email']

@admin.register(Products)
class ProductsTable(admin.ModelAdmin):
    list_display = ['Username', 'phone_no', 'Product_name']
