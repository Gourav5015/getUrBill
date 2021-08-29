from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Accounts,Items
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

def home(request):
    if (request.method=="POST"):
        phone_number=request.POST["phone_number"]
        passwd=request.POST["password"]
        user=authenticate(username=phone_number,password=passwd)
        if user is not None:
            login(request,user)
            return redirect("/dashboard/")
        return redirect("/")
    return render(request,"index.html")

@login_required
def dashboard(request):
    if request.method=="POST":
        c=request.POST['count']
        c=int(c)
        for i in range(0,c+1):
            item_name=request.POST['item_name'+str(i)]
            quantity=request.POST['quantity'+str(i)]
            discount=request.POST['discount'+str(i)]
            gst=request.POST['gst'+str(i)]
            price=request.POST['price'+str(i)]
            user=request.user
            item=Items(user=user,item_name=item_name,quantity=quantity,GST=gst,discount=discount,selling_price=price)
            item.save()
        return redirect("/dashboard/")
    items=Items.objects.all().filter(user=request.user)
    context={"i":items}
    return render(request ,"dashboard.html",context)

def Logout(request):
    logout(request)
    return redirect("/")

def delete(request,k):
    item=Items.objects.all().filter(item_name =k)
    item.delete()
    return redirect("/dashboard/")

