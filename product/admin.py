from django.contrib import admin
from django.apps import apps

# Register your models here.
from .models import Product,Customer
admin.site.register(Product)
admin.site.register(Customer) 

