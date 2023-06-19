# Create your views here.
# function based views 

from django.shortcuts import render
from .models import Product
from product.forms import CustomerAddForm  

def product(request):
    products= Product.objects.all() #ORM -- object related maping - grabbing the databse from the products. 
    return render(request,'product.html', {'products':products}) 

def home(request):
    products= Product.objects.all() #ORM -- object related maping - grabbing the databse from the products. 
    return render(request,'home.html', {'products':products}) 

def product_detail(request,pk):
    form=CustomerAddForm()
    product= Product.objects.get(id=pk) #pk -- primary key  
    return render(request,'product-detail.html',{'product':product,"form":form}) 

from django.contrib import messages
from django.shortcuts import redirect

def save_customer_order(request):
    if request.method == "POST":
        form = CustomerAddForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order placed successfully")
            return redirect(f"/product/{form.cleaned_data.get('product').id}")
        messages.error(request, form.errors)
        return redirect(f"/product/{form.cleaned_data.get('product').id}")
