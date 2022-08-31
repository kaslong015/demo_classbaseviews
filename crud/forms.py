from dataclasses import fields
from django import forms
from crud.models import Customer


class CreateCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'age', 'Address']
