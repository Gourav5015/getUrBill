"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GetUrBill import views
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('dashboard/',views.dashboard),
    path("logout/",views.Logout),
    path("delete/<str:k>",views.delete,name="delete"),
    path("edit/<str:k>",views.edit,name="edit"),
    path('register/',views.register),
    path('registeruser/',views.registeruser),
    path('check/<str:phone>/',views.check),
    path('bill/',views.bill),
    path('createbill/<str:c>/<str:b>/',views.createbill),
    path('account/',views.myaccount),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/',(admin.site.urls)),
    path('ajaxitem/',views.ajaxadditem),
    path('checkquantity/<str:item>/',views.checkquantity),
    path('generate/<str:bill>/',views.generateview),
    path('<str:phonenumber>/<str:b>/d/<str:id>/',views.deleteitem),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)