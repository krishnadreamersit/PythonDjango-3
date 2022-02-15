from django import forms

class EmployeeForm(forms.Form):
    full_name = forms.CharField()
    contact_address = forms.CharField()
    mobile = forms.CharField()
    email = forms.CharField()
