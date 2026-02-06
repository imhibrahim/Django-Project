from django import forms

class personform(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    mail=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))