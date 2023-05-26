from django.urls import path
from products.views import all_products , show_product , delete_product , show_category , add_product

urlpatterns = [
    path('products/', all_products, name="home"),
    path('products/<int:id>', show_product, name="show"),
    path('products/delete/<int:id>', delete_product, name="delete"),
    path('category/<int:id>', show_category, name="category"),
    path('add', add_product, name="add"),
]
