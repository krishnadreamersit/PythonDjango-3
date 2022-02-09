from django import forms

class PersonForm(forms.Form):
    pid = forms.IntegerField()
    fullname = forms.CharField()
    contactaddress = forms.CharField()