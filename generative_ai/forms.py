from django import forms


class BusinessForm(forms.Form):
    industry = forms.CharField(max_length=500)
    audience = forms.CharField(max_length=500)
    budget = forms.CharField(max_length=20)
