from django.shortcuts import render
def home(request):
    return render(request,"index.html")
def dashboard(request):
    a={"name":"gargi"}
    return render(request ,"dashboard.html",a)