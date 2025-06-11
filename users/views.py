from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_user_view(request):
    return render(request, 'users/register_user.html')

def login_user_view(request):
    return render(request, 'users/login_user.html')

def logout_user_view(request):
    logout(request)
    messages.success(request, "You are logged out successfully")
    return redirect("/login_user/")
  
