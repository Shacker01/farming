from django import forms
from . models import Treatment, Farmers, Products, Medicines


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'

class FarmersForm(forms.ModelForm):
    class Meta:
        model = Farmers
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        
class MedicinesForm(forms.ModelForm):
    class Meta:
        model = Medicines
        fields = '__all__'