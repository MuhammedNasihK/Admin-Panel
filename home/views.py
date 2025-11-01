from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import Registerform,Loginform,Add_user_form

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


def loginv(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                get = User.objects.get(username=username)

            except User.DoesNotExist:
                form.add_error(None,'User not exist')
                return render(request,'login.html',{'form':form})

            password = form.cleaned_data['password']
            if get.check_password(password):
                request.session['user_id'] = get.id
                return redirect('admin')  
            else:
                form.add_error('password',"Wrong password")
                return render(request,'login.html',{'form':form})


    form = Loginform()

    return render(request,'login.html',{'form':form})

def admin(request):
    if 'user_id' not in request.session:
        return redirect('login')
    data = User.objects.all()

    dict = {
        'data' : data
    }
    return render(request,'admin_page.html',dict)


def add_user(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    if request.method == 'POST':
        form = Add_user_form(request.POST)
        if form.is_valid():
            data = form.save(commit = False)
            password = form.cleaned_data['password']
            data.set_password(password)
            data.save()
            
    form = Add_user_form()


    return render(request,'add_user.html',{'form':form})