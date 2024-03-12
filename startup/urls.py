"""
URL configuration for startup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include


from .views import *
from insti_app.views import mentor_reg_view,submit_view,mentee_reg_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path("", home_page,name='home_name'),
    path('institutes/', include('insti_app.urls')),
    path('booking/', include('book.urls')),
    path('mentor_reg',mentor_reg_view,name="mentor_reg_url"),
    path('mentee_reg',mentee_reg_view,name="mentee_reg_url"),
    path("submit",submit_view,name='submit_view'),
    path("dashboard",dashboard_view,name='dashboard_name'),
    path('privacypolicy',privacy_view,name="privacy name"),
    path('termsofservice',terms_view,name="terms name"),  
    path("demo", demo_view,name='demo_name'),
 
    path("payment",payment_view,name="payment name"),
    path("success",success_view,name="success name"),
    path("book",book_appoint,name="book_name"),
    path("bookpayment",paymentbook,name="payment_book"),
]
