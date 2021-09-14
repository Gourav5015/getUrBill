from django.contrib import admin
from .models import Accounts,Items,Bill_no,Billitems,Customer
from .forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import Http404, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import AdminPasswordChangeForm
# Register your models here.

class billinline(admin.TabularInline):
    model=Billitems
class itemsinline(admin.TabularInline):
    model=Items


@admin.register(Bill_no)
class customer(admin.ModelAdmin):
    inlines=(billinline,)
@admin.register(Accounts)
class UserAdmin(BaseUserAdmin):
    model=Accounts
    inlines=(itemsinline,)
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ( 'phoneNumber', 'shop_name','pincode','verification','is_staff')
    list_filter = ('phoneNumber',"shop_name")
    fieldsets = (
        (None, {'fields': ('phoneNumber', 'password')}),
        ('Personal info', {'fields': ('first_name','email','shop_name','Address','pincode','verification')}),
         ('Permissions', {'fields': ('is_staff','is_active','is_superuser', 'groups', 'user_permissions')}),
         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phoneNumber','first_name','shop_name','password1','password2')}
        ),
        
    )
    search_fields = ('phoneNumber','shop_name')
    ordering = ('phoneNumber','shop_name','is_staff')
    filter_horizontal = ()


admin.site.register((Items,Billitems,Customer,Session))

admin.site.site_title="GetUrBill"
admin.site.site_header="GetUrBill"
admin.site.index_title="GetUrBill Admin Portal"
admin.site.enable_nav_sidebar=True