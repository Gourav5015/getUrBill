from django.contrib import admin
from .models import Accounts,Items,Bill_no,Bill_items,Customer
# Register your models here.
admin.site.register((Accounts,Items,Bill_no,Bill_items,Customer))

admin.site.site_title="GetUrBill"
admin.site.site_header="GetUrBill"
admin.site.index_title="GetUrBill Admin Portal"
admin.site.enable_nav_sidebar=True