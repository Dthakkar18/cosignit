from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from json import dumps
from .models import Member
from django.contrib.auth.models import User


# Create your views here.

# hello world view
def login_signup_user(request):
    if request.method == 'POST':
        # handling signup
        if request.POST.get("Signup_User"): # if signup button
            firstName = request.POST.get("First_Name")
            lastName = request.POST.get("Last_Name")
            username = request.POST.get("Username")
            email = request.POST.get("Email_Address")
            password = request.POST.get("Password")
            confirm_password = request.POST.get("Confirm_password")
            # check password length
            if len(password) < 10:
                context = {
                    'login_display': "Signup requirements not met!",
                    'signup_display': "Password must be at least 10 characters!"
                }
                return render(request, "myapp/login_user.html", context)
            # check password matches confirm password
            if password != confirm_password:
                context = {
                    'login_display': "Signup requirements not met!",
                    'signup_display': "Make sure to retype same password!"
                }
                return render(request, "myapp/login_user.html", context)
            # check if email is being reused
            try:
                user = User.objects.get(email=email)
                #member = Member.objects.get(email=email)
                if user:
                    print("Email is already in use!")
                    context = {
                        'login_display': "Signup requirements not met!",
                        'signup_display': "Account with email already exists!"
                    }
                    return render(request, "myapp/login_user.html", context)
            except:
                # means there isn't a user with the email provided
                pass
            # check if username is being reused
            try:
                user = User.objects.get(username=username)
                #member = Member.objects.get(email=email)
                if user:
                    print("Username is already in use!")
                    context = {
                        'login_display': "Signup requirements not met!",
                        'signup_display': "Account with username already exists!"
                    }
                    return render(request, "myapp/login_user.html", context)
            except:
                # means there isn't a user with the email provided
                pass
            # make the new user
            created_user = User.objects.create_user(
                first_name = firstName,
                last_name = lastName,
                username = username,
                email = email,
                password = password
            )
            Member.objects.create(
                user = created_user # attaching the user to the member (oneToOne model)
            )
            print("Created user: " + firstName + " " + lastName)

        if request.POST.get("Login_User"): # if login button
            username = request.POST.get("Username")
            password = request.POST.get("Password")
            # authenticate user
            user = authenticate(username=username, password=password)
            if user is None:
                context = {
                    'login_display': "Incorrect username/password!"
                }
                return render(request, "myapp/login_user.html", context)
            print(f"Authenticated user: {user}")

            """
            # check if correct credentials
            try:
                member = Member.objects.get(email=email)
                if member.password != password:
                    context = {
                        'login_display': "Incorrect username/password!"
                    }
                    return render(request, "myapp/login_user.html", context)
            except:
                # means there isn't a member with the email provided
                context = {
                        'login_display': "Incorrect email/password!"
                    }
                return render(request, "myapp/login_user.html", context)"""


            # login the member
            login(request, user=user)
            # redirect to homepage
            return redirect(home_page_user)
         
    
    # regular page endpoint
    return render(request, "myapp/login_user.html", {})

@login_required
def home_page_user(request):
    username = request.user.username
    context = {
        "username": username
    }
    return render(request, "myapp/home_page_user.html", context)

def logout_user(request):
    logout(request)
    print("user logged out")
    return redirect(login_signup_user)




def login_signup_store(request):
    if request.method == 'POST':
        # handling signup
        if request.POST.get("Signup_Store"): # if signup button
            storeName = request.POST.get("Store_Name")
            email = request.POST.get("Email_Address")
            password = request.POST.get("Password")
            confirm_password = request.POST.get("Confirm_password")
            # check password length
            if len(password) < 10:
                context = {
                    'login_display': "Signup requirements not met!",
                    'signup_display': "Password must be at least 10 characters!"
                }
                return render(request, "myapp/login_store.html", context)
            # check password matches confirm password
            if password != confirm_password:
                context = {
                    'login_display': "Signup requirements not met!",
                    'signup_display': "Make sure to retype same password!"
                }
                return render(request, "myapp/login_store.html", context)
            # check if email is being reused
            try:
                user = User.objects.get(email=email)
                #member = Member.objects.get(email=email)
                if user:
                    print("Email is already in use!")
                    context = {
                        'login_display': "Signup requirements not met!",
                        'signup_display': "Account with email already exists!"
                    }
                    return render(request, "myapp/login_store.html", context)
            except:
                # means there isn't a user with the email provided
                pass
            # check if store name is being reused
            try:
                user = User.objects.get(storeName=storeName)
                if user:
                    print("Store name is already in use!")
                    context = {
                        'login_display': "Signup requirements not met!",
                        'signup_display': "Account with this store name already exists!"
                    }
                    return render(request, "myapp/login_store.html", context)
            except:
                # means there isn't a user with the email provided
                pass
            # make the new user
            User.objects.create(
                email = email,
                password = password,
                storeName = storeName
            )
            print("Created store: " + storeName)

        if request.POST.get("Login_Store"): # if login button
            storeName = request.POST.get("Store_Name")
            password = request.POST.get("Password")

            # authenticate store (thinking to have store name = username)
            """user = authenticate(username=storeName, password=password)
            if user is None:
                context = {
                    'login_display': "Incorrect store name/password!"
                }
                return render(request, "myapp/login_store.html", context)
            print(f"Authenticated user: {user}")

            # login the store
            login(request, user=user)"""


            # redirect to homepage
            return redirect(home_page_store)
         
    
    # regular page endpoint
    return render(request, "myapp/login_store.html", {})


#@login_required
def home_page_store(request):
    storeName = request.user.storeName
    context = {
        "storeName": storeName
    }
    return render(request, "myapp/sample.html", storeName)

# using reactpy 
def reactpy_sample(request):
    context={}
    return render(request, "myapp/reactpy_basic.html", context)