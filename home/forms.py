from django import forms
from django.contrib.auth import get_user_model



User = get_user_model()

class Registerform(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'class_name','placeholder':'Username'}))

    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'class_name','placeholder':'Email'}))

    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'class_name','placeholder':'Password'}))

    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'class_name','placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username','email','password']
   
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('confirm_password')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match')
        
        return cleaned_data


class Loginform(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'class_name' , 'placeholder':'Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'class_name' , 'placeholder':'Password'}))

    
        