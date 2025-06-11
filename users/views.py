from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_user_view(request):
    profile = Profile.objects.last()
    if request.method=="POST":
        data = request.POST
        un = data.get("uname")
        psw = data.get("password")
        cps = data.get("cpassword")
        email=data.get("eml")
        fn=data.get("fname")
        ln=data.get("lname")
        pro_pic=request.FILES.get("profile")
        mobile=data.get("mobile")
        if psw!=cps:
            messages.warning(request, "Password and confirm password not matching")
            return redirect("/register_user/")
        user = User.objects.create_user(username=un, password=psw, first_name=fn, last_name=ln, email=email)
        profile = Profile(user=user, mobile=mobile, profile_pic=pro_pic)
        profile.save()
        messages.success(request, "Your account has been created successfully")
    return render(request, 'users/register_user.html', {'profile': profile})

def login_user_view(request):
    if request.method=="POST":
        data = request.POST
        un = data.get("uname")
        psw = data.get("password")
        
        user = authenticate(request, username=un, password=psw)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully")
            return redirect("/login_user/")

        else:
            messages.warning(request, "invalid credentials")
            return redirect("/login_user/")
    return render(request, 'users/login_user.html')

def logout_user_view(request):
    logout(request)
    messages.success(request, "You are logged out successfully")
    return redirect("/login_user/")
  
