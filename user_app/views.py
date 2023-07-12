from django.shortcuts import render, HttpResponse, redirect
from .forms import NewUserForm  # username, email, pass1, pass2
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def user_signup(request):
    if request.method == "POST":
        data = request.POST
        print(data, "Data")
        form = NewUserForm(data)
        if form.is_valid():
            user = form.save()  # user entry in auth_user table
            print(user)   #AparnaH
            messages.success(request, f"User '{user.username}' registered successfully. You can login here." )
            return redirect("user_login")
        else:
            messages.error(request, "Unsuccessful signup. Invalid information.")
    elif request.method == "GET":
        form = NewUserForm()
        return render(request=request, template_name="register.html", context={"signup_form":form})
    

def user_login(request):
    if request.method == "POST":
        # form = AuthenticationForm(request, data=request.POST)  # username, password
        # if form.is_valid():
        #     user_name = form.cleaned_data.get("username")  # KapilD
        #     password = form.cleaned_data.get("password")    # Python@123
        #     print(user_name, password)
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        print(user_name, password)
        user = authenticate(username=user_name, password=password)  # verify -- auth_user -- return user object
        if user:
            login(request, user)   # session maintain -- django session table
            messages.success(request, "Logged in succesfully.")
            return redirect("home_page")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("user_login")


    elif request.method == "GET":
        return render(request, "login.html", {"login_form": AuthenticationForm()})

def user_logout(request):
    logout(request)
    return redirect("user_login")


def user_check_login(request):
    pass