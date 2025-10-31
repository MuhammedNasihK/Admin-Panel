from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import Registerform,Loginform

# Create your views here.

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            userd = form.save(commit=False)
            password = form.cleaned_data['password']
            userd.set_password(password)
            userd.save()
            return redirect('login')
    else:
        form = Registerform()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        exist = User.objects.filter(username=username).exists()

        if exist:
            user_data = User.objects.get(username=username)

    form = Loginform()

    return render(request,'login.html',{'form':form})

def admin(request):
    return render(request,'admin_page.html')