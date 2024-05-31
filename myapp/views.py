from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from json import dumps
from .models import Member

# Create your views here.

# hello world view
def login_signup(request):
    if request.method == 'POST':
        # handling signup
        if request.POST.get("Signup"): # if signup button
            firstName = request.POST.get("First_Name")
            lastName = request.POST.get("Last_Name")
            email = request.POST.get("Email_Address")
            password = request.POST.get("Password")
            confirm_password = request.POST.get("Confirm_password")
            date = request.POST.get("date")
            # check password length
            if len(password) < 10:
                context = {
                    'login_display': "Signup requirements not met!",
                    'signup_display': "Password must be at least 10 characters!"
                }
                return render(request, "myapp/login.html", context)
            # check password matches confirm password
            if password != confirm_password:
                context = {
                    'login_display': "Signup requirements not met!",
                    'signup_display': "Make sure to retype same password!"
                }
                return render(request, "myapp/login.html", context)
            # check if email is being reused
            try:
                member = Member.objects.get(email=email)
                if member:
                    print("Email is already in use!")
                    context = {
                        'login_display': "Signup requirements not met!",
                        'signup_display': "Account with email already exists!"
                    }
                    return render(request, "myapp/login.html", context)
            except:
                # means there isn't a member with the email provided
                pass
            # make the new Member
            Member.objects.create(
                firstName = firstName,
                lastName = lastName,
                email = email,
                password = password,
                birthday = date
            )
            print("Created member: " + firstName + " " + lastName)
        if request.POST.get("Login"): # if login button
            email = request.POST.get("Email_Address")
            password = request.POST.get("Password")
            # check if correct credentials
            try:
                member = Member.objects.get(email=email)
                if member.password != password:
                    context = {
                        'login_display': "Incorrect email/password!"
                    }
                    return render(request, "myapp/login.html", context)
            except:
                # means there isn't a member with the email provided
                context = {
                        'login_display': "Incorrect email/password!"
                    }
                return render(request, "myapp/login.html", context)
            # login the member
            print(member)
         
    
    # regular page endpoint
    return render(request, "myapp/login.html", {})

# first sample view
def home_page(request):
    context = {

    }
    return render(request, "myapp/home_page.html", context)