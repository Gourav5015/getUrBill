from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
from .models import Accounts, Bill_no, Customer,Items
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .forms import UserCreationForm
from management import settings
from django.contrib import messages
from django.http import JsonResponse
import random,datetime

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
    #items=Items.objects.all().filter(user=request.user)
    items=request.user.items_set.all()
    context={"i":items}
    return render(request ,"dashboard.html",context)

def Logout(request):
    logout(request)
    return redirect("/")

def delete(request,k):
    item=Items.objects.all().filter(item_id =int(k))
    item.delete()
    return redirect("/dashboard/")

def edit(request,k):
    i=Items.objects.all().filter(item_id =int(k)).first()
    context={"item":i}
    if request.method=="POST":

        item_name=request.POST['item_name']
        quantity=request.POST['quantity']
        discount=request.POST['discount']
        gst=request.POST['gst']
        price=request.POST['price']
        user=request.user
        item=Items(item_id=i.item_id,user=request.user,item_name=item_name,quantity=quantity,GST=gst,discount=discount,selling_price=price)
        item.save()
        return redirect ("/dashboard/")

    if i:
        return render (request ,"edit.html",context)

    else:
        return redirect("/dashboard/")

@staff_member_required
def register(request):
    return render(request,"register.html")
@staff_member_required
def registeruser(request):
    if request.method=='POST':
        password=request.POST['password']
        staff=authenticate(username=request.user.phoneNumber,password=password)
        if staff is not None:
            phone_number=request.POST['phone number']
            first_name=request.POST['first name']
            shop_name=request.POST['shop name']
            password1=request.POST['password1']
            password2=request.POST['password2']
            if password1==password2:
                username=Accounts.objects.all().filter(phoneNumber=phone_number).first()
            
                if username is None:
                    user=Accounts.objects.create_user(phoneNumber=phone_number,password=password1,first_name=first_name,shop_name=shop_name)
                    user.save()
                    messages.error(request,"Registered Successfully")
                    return redirect("/register/")
                else :
                    messages.error(request,"phone number exists")
                    return redirect("/register/")
        else:
            messages.error(request,"enter correct password or contact your admin")
            return redirect("/register/")
def check(request,phone):
    user=Accounts.objects.all().filter(phoneNumber=phone).first()
    if user:
        return JsonResponse({"status":"Phone Number Exists"})
    else:
        return JsonResponse( {"status":"OK"})


def bill(request):
    items=request.user.items_set.all()
    if request.method=="POST":
        name=request.POST['name']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        customer= request.user.customer_set.create(name=name,email=email,contact_no=phonenumber)
        bill_num=customer.bill_no_set.create(user=request.user,shop_name=request.user.shop_name,Address=request.user.Address,bill_no=billno(request))
        return redirect("/createbill/"+str(phonenumber)+"/"+str(bill_num.bill_no)+"/")
    return render (request, "bill.html",{"i":items})

def myaccount(request):
    return render (request, "myaccount.html")

# bill no function
def billno(request):
    b=str(request.user.shop_name)+"-"+str(datetime.date.today())+"-"+ str(random.randint(10000,100000))
    return b
def finalprice(price,discount):
    return price-(discount*price/100)
def createbill(request,c,b):
    customer=request.user.customer_set.all().filter(contact_no=c).last()
    bill_num=customer.bill_no_set.all().filter(bill_no=b).first()
    items=request.user.items_set.all()
    billitem=bill_num.billitems_set.all()
    if(request.method=="POST"):
        itemname=request.POST["itemselected"]
        quantity=request.POST["quantity"]
        bill_number=request.POST["bill number"]
        item_name=request.user.items_set.all().filter(item_name=itemname).first()
        bill_n=request.user.bill_no_set.all().filter(bill_no=bill_number).first()
        price=int (item_name.selling_price)
        price=(price*int(quantity))
        item_name.quantity=int(item_name.quantity)-int(quantity)
        item_name.save()
        bill_n.billitems_set.create(item_name=itemname,quantity=quantity,price=price,discount=item_name.discount,Final_price=finalprice(price,item_name.discount))
        

    return render (request,"newbill.html",{"bill_number":bill_num,"customer":customer,"item":items,"bitem":billitem})

    