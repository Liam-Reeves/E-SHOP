from django import forms
from .models import Newsletter
from django.forms import ModelForm


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email',]
        
    email = forms.EmailField(
        widget  = forms.EmailInput(
            attrs= {
                'placeholder': 'Enter your email address',
                'class': 'email-input',
                      
                }
            ))