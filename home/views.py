from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import Registerform,Loginform,Add_user_form
from django.http import HttpResponse

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
                request.session.set_expiry(0)
                return redirect('admin')  
            else:
                form.add_error('password',"Wrong password")
                return render(request,'login.html',{'form':form})

    form = Loginform()

    return render(request,'login.html',{'form':form})



def logout(request):
    if 'user_id' not in request.session:
        return redirect('login')
       
    if request.method == 'POST':
        del request.session['user_id']
        return redirect('login')
       


def admin(request):
    if 'user_id' not in request.session:
        return redirect('login')
    data = User.objects.all()
    dict = {
        'data' : data,
    }
    return render(request,'admin_page.html',dict)


def add_user(request):
    if 'user_id' not in request.session:
        return redirect('login')
    form = Add_user_form()
    
    if request.method == 'POST':
        form = Add_user_form(request.POST)
        if form.is_valid():
            data = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                form.add_error('username','Username already exist')
                return render(request,'add_user',{'form':form})
            data.set_password(password)
            data.save()
            return redirect('admin')
            
    
    return render(request,'add_user.html',{'form':form})



def edit(request,id):
    old_data = User.objects.get(id=id)
    
    form = Add_user_form(instance=old_data)
   
    if request.method == 'POST':
        form = Add_user_form(request.POST,instance=old_data)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            data = User.objects.get(id=id)
            check = User.objects.filter(username=username).exclude(id=id).exists()

            if check:
                form.add_error('username','Username already exist')
                return render(request,'edit.html',{'form':form})
            
            elif User.objects.filter(email=email).exclude(id=id).exists():
                form.add_error('email','User with this email exist')
                return render(request,'edit.html',{'form':form})
                
            
            data.username = username
            data.email = email
            data.set_password(password)

            data.save()
            return redirect('admin')
            
    
    return render(request,'edit.html',{'form':form})


def delete(request,id):
   data = User.objects.get(id=id)
   data.delete()
   return redirect('admin')