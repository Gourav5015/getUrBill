from django.contrib import admin
from .models import Accounts,Items
# Register your models here.
admin.site.register((Accounts,Items))