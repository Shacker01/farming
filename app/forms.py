from django import forms
from . models import Treatment, Farmer, Products


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'