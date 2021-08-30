from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
import random
from datetime import datetime

from .manager import CustomUserManager
# Create your models here.
class Accounts(AbstractUser):
    username=None
    verification=models.BooleanField(default=False)
    phoneNumber=models.CharField (_('phone_number'),unique=True,max_length=10)
    shop_name=models.CharField(max_length=50)
    Address=models.TextField(default="")
    pincode=models.IntegerField(null=True)
    USERNAME_FIELD="phoneNumber"
    REQUIRED_FIELDS=["first_name","shop_name"]
    objects=CustomUserManager()

    def __str__(self):
        return self.first_name+" "+self.last_name

class Items(models.Model):
    item_id=models.BigAutoField(primary_key=True)
    user=models.ForeignKey(Accounts,on_delete=CASCADE)
    item_name=models.CharField(max_length=100)
    quantity=models.IntegerField(default=0)
    selling_price=models.IntegerField(default=0)
    GST=models.IntegerField(default=9)
    discount=models.IntegerField(default=0)

    def __str__(self):
        return self.item_name+" "+self.user.first_name+" "+self.user.last_name


class Customer(models.Model):
    user=models.ForeignKey(Accounts,on_delete=CASCADE)
    name=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=12)
    email=models.CharField(default=" ",max_length=50)
    paid=models.IntegerField(default=0)
    due=models.IntegerField(default=0)
    customer_id=models.IntegerField(default=random.randint(100000,999999))
    def __str__(self):
        return str(self.customer_id) +" "+self.name


class Bill_no(models.Model):
    user=models.ForeignKey(Accounts,on_delete=CASCADE)
    customer=models.ForeignKey(Customer,on_delete=CASCADE)
    bill_no=models.CharField(max_length=100,primary_key=True)
    shop_name=models.CharField(max_length=50)
    Address=models.TextField(default="")
    date_of_purchase=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.bill_no

class Bill_items(models.Model):
    bill_no=models.ForeignKey(Bill_no,on_delete=CASCADE)
    item_name=models.CharField(max_length=100)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    Final_price=models.IntegerField(default=0)
    def __str__(self):
        return self.bill_no.bill_no +" "+ self.item_name

