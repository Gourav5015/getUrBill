from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
from .models import Accounts,Items
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .forms import UserCreationForm
from management import settings
from django.contrib import messages

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

        item_name=request.POST['item_name']
        quantity=request.POST['quantity']
        discount=request.POST['discount']
        gst=request.POST['gst']
        price=request.POST['price']
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
    item=Items.objects.all().filter(item_id =int(k))
    item.delete()
    return redirect("/dashboard/")

@staff_member_required
def register(request):
    return render(request,"register.html")
@staff_member_required
def registeruser(request):
    if request.method=='POST':
        phone_number=request.POST['phone number']
        first_name=request.POST['first name']
        shop_name=request.POST['shop name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            username=Accounts.objects.all().filter(phoneNumber=phone_number).first()
            print(username)
            if username is None:
                user=Accounts.objects.create_user(phoneNumber=phone_number,password=password1,first_name=first_name,shop_name=shop_name)
                user.save()
                messages.error(request,"Registered Successfully")
                return redirect("/register/")
            else :
                messages.error(request,"phone number exists")
                return redirect("/register/")
   