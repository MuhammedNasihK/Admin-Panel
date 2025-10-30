from django import forms
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
class Registerform(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'class_name','placeholder':'Password'}))

    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'class_name','placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username','email','password']

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'class_name','placeholder' : 'Username'}),
            'email' : forms.EmailInput(attrs={'class' : 'class_name','placeholder': 'Email:'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('confirm_password')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Password do not match')
        
        return cleaned_data

        