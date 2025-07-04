from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'post':
      form = CustomUserCreationForm(request.Post)
      if form.is_valid():
        user = form.save()
        auth_login(request,user)
        return redirect('home')
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form':form})
    
