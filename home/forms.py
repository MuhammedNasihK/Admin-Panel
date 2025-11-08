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
        username = cleaned_data['username']
        if len(username) <= 3:
            raise forms.ValidationError('Username must contain four values')
        elif username.isdigit():
            raise forms.ValidationError('Username must contain characters')
        elif len(p1) <= 3:
            raise forms.ValidationError('password must countain four values')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match')
        
        return cleaned_data


class Loginform(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'class_name' , 'placeholder':'Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'class_name' , 'placeholder':'Password'}))


class Add_user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Username' , 'class':'class_name'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Email' , 'class':'class_name'}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Password','class':'class_name'})
        }


class Edit_user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Username' , 'class':'class_name'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Email' , 'class':'class_name'}),
        }      