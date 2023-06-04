from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from products.models import Product, Category
from .forms import ProductForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status



# products = [
#     {'name':"Apple" ,"price" : 24},
#     {'name':"Samsung" ,"price" :26},
#     {'name':"Lenovo",  "price" :20}
# ]

def all_products(request):
    products = Product.get_products()
    return render(request, "products/index.html", context={"products": products})


def show_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/show.html", context={"product": product})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect(reverse('home'))


def show_category(request, id):
    category = Category.get_category(id)
    print(category)
    products = category.get_products
    print(products)
    return render(request, "products/category.html", context={"category": category, "products": products})


def add_product(request):
    url = "products/addProduct.html"
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
        else:
            print("Invalid")
            return render(request, url , context={"form": form})
        
    form = ProductForm()
    return render(request, url , context={"form": form})

def edit_product(request, id):
    url = "products/addProduct.html"
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
            form = ProductForm(request.POST , request.FILES , instance = product)
            if form.is_valid():
                form.save()
                return redirect(reverse('home'))
            else:
                return render(request, url, context = {"form" : form})
    else:
        form = ProductForm(instance = product)
        return render(request, url, context={"form": form})        

@api_view(['GET' , 'POST'])
def all_of_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        my_serialzer = ProductSerializer(products , many=True)
        return Response(my_serialzer.data , status= status.HTTP_200_OK) 
    
    if request.method == "POST":
          my_serializer = ProductSerializer(data = request.data)
          if my_serializer.is_valid():
                my_serializer.save()
                return Response(my_serializer.data , status = status.HTTP_200_OK)
          else:
               return Response({"message": "Invalid data"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET' , 'PUT' , 'DELETE'])
def one_product(request , id ):
    try:
                product = get_object_or_404(Product, id=id)
    except:
               return Response({"message": "product not found"}, status = status.HTTP_404_NOT_FOUND)  
      
    if request.method == "GET":
             my_serializer = ProductSerializer(product)
             return Response(my_serializer.data , status= status.HTTP_200_OK)
 
    if request.method == "PUT":
            my_serializer = ProductSerializer(product, data = request.data , partial = True)
            if my_serializer.is_valid():
                 my_serializer.save()
                 return Response(my_serializer.data , status = status.HTTP_200_OK)
            else:
                 return Response({"message": "Invalid data"}, status = status.HTTP_400_BAD_REQUEST)
            
    if request.method == "DELETE":
         my_serializer = ProductSerializer(product)
         product.delete()
         return Response({"message": "Product deleted"}, status = status.HTTP_200_OK)          
     
          
     
