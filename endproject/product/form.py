from django import forms

class productform(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    pic=forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))