from django import forms

class personform(forms.Form):
    name=forms.CharField(max_length=100)
    mail=forms.EmailField()
    age=forms.IntegerField()