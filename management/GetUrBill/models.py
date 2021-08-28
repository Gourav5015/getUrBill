from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _

from .manager import CustomUserManager
# Create your models here.
class Accounts(AbstractUser):
    username=None
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
    user=models.ForeignKey(Accounts,on_delete=CASCADE)
    item_name=models.CharField(max_length=100)
    quantity=models.IntegerField(default=0)
    selling_price=models.IntegerField(default=0)
    GST=models.IntegerField(default=9)
    discount=models.IntegerField(default=0)

    def __str__(self):
        return self.item_name+" "+self.user.first_name+" "+self.user.last_name