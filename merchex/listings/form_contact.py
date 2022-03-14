from dataclasses import field
import email
from email import message
from django import forms
from listings.models import Band, Listing


class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = "__all__"