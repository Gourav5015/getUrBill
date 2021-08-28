from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Accounts
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
def home(request):
    if (request.method=="POST"):
        phone_number=request.POST["phone_number"]
        password=request.POST["password"]
        user=authenticate(phoneNumber=phone_number,password=password)
        if user is not None:
            login(request,user)
            return redirect("/dashboard/")
        return redirect("/")
    return render(request,"index.html")
def dashboard(request):
    return render(request ,"dashboard.html")

def Logout(request):
    logout(request)
    return redirect("/")
