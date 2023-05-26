from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse 
from products.models import Product , Category 
from .forms import ProductForm
# products = [
#     {'name':"Apple" ,"price" : 24},
#     {'name':"Samsung" ,"price" :26},
#     {'name':"Lenovo",  "price" :20}
# ]

def all_products(request):
    products= Product.get_products()
    return render(request, "products/index.html" ,context={"products":products})

def show_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request ,"products/show.html", context={"product":product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect(reverse('home'))

def show_category(request, id):
    category = Category.get_category(id)
    print(category)
    products = category.get_products
    print(products)
    return render(request, "products/category.html", context={"category":category , "products":products})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST , request.FILES)
        if form.is_valid():
            category = Category.get_category(form.cleaned_data["category"])
            Product.objects.create(name = form.cleaned_data['name'], price = form.cleaned_data['price'], category = category , img = form.cleaned_data['img']) 
            return redirect(reverse('home'))
        else:
            print("Invalid")
            return render(request, "products/addProduct.html", context={"form":form})               
    form = ProductForm()
    return render(request, "products/addProduct.html", context={"form":form})