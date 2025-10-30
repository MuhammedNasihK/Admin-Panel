from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import Registerform

# Create your views here.

User = get_user_model()

def register(request):
    form = Registerform()
    if request.method == 'POST':
        form = Registerform(request.POST)
        user = form.save(commit=False)
        password = user.cleaned_data['password']
        user.set_password(password)
        user.save()
    
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def admin(request):
    return render(request,'admin_page.html')