from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
class UserForm(ModelForm):
    class Meta:
        model=User
        fields=("username", "email","first_name","last_name","password")
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder':'Type your name','label':None})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Type your email'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'Type your first name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Type your last name'})
        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Enter your password'})