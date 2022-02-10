from django import forms
from app4_1.models import Person

# ModelForm (Model and Form)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

