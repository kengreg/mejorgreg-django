'''
Created on Dec 10, 2014

@author: kengreg
'''
from django import forms
from django.forms import ModelForm
from htmlpublic.models import Enlace

class EnlaceForm(forms.ModelForm):
    class Meta:
        model = Enlace
        exclude = ("votos",)
