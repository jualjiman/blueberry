# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Nombre*','class':'form-control validate[required]'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email*','class':'form-control validate[required,custom[email]]'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Asunto','class':'form-control'}))

    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensaje','class':'form-control validate[required]','rows':'5'}))