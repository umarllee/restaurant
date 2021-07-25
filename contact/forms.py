from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name_surname= forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Name and Surname'
    }))
    email= forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 
        'placeholder': 'E-mail'
    }))
    message= forms.CharField(
        widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Message'
    })
    )

    class Meta:
        model =Contact
        fields= [ 'name_surname' , 'email' , 'message' ]
