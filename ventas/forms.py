from django import forms
from ventas.models import *


class AddproductForm(forms.ModelForm):

    class Meta:
        model = Producto
        exclude = {'status',}
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Adam Fernandez"
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3'
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'plaseholder': '0.00'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }




# class AddproductForm(forms.Form):
#     nombre = forms.CharField(widget=forms.TextInput)
#     descripcion = forms.CharField(widget=forms.TextInput)
#     imagen = forms.ImageField(required=False)
#     precio = forms.DecimalField(required=True)
#     stock = forms.IntegerField(required=True)
#
#     def clean(self):
#         return self.cleaned_data