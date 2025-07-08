from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomRegisterForm, CustomLoginForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home') 
    else:
      form = CustomUserCreationForm()
      return render(request, 'register.html', {'form':form})      

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})





def custom_register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1']
            )
            auth_login(request, user)
            return redirect('custom_home')
    else:
        form = CustomRegisterForm()
    return render(request, 'custom_register.html', {'form': form})


    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username= form.cleaned_data['username'],
                email= form.cleaned_data['email'],
                first_name= form.cleaned_data['first_name'],
                last_name= form.cleaned_data['last_name'],
                password= form.cleaned_data['password1']
            )
            auth_login(request, user)
            return redirect('home')
        else:
            form = CustomRegisterForm()
        return render(request, 'custom_register.html', {'form':form})
    return HttpResponse('This is it ')
        
def custom_login(request):
    error = None
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('custom_home')
            else:
                error = 'Invalid username or password'
    else:
        form = CustomLoginForm()
    return render(request, 'custom_login.html', {'form': form, 'error': error})


    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                error = 'Invalid username or password'
        else:
            form = CustomLoginForm()
        return render(request, 'custom_login.html', {'form': form, 'error' :error})
    

def home(request):
    return render(request, 'home.html')