from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100 , null=True, blank= True)

    @classmethod
    def get_categories(cls):
        return cls.objects.all()
    
    @classmethod
    def get_category(cls,id):
        return cls.objects.filter(id=id).first()
    
    @property
    def get_products(self):
        products = self.products.all()
        return products

    @property
    def show_url(self):
        return reverse( 'category' , args=[self.id])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100 , null= False , blank= True)
    price = models.IntegerField(blank=True)
    img= models.ImageField(null= True, blank= True , upload_to='media/')    
    created_at = models.DateTimeField(auto_now_add=True , null= True)
    updated_at = models.DateTimeField(auto_now = True, null= True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='products')

    @classmethod
    def get_products(cls):
        return cls.objects.all()

    @property
    def image(self):
        return f"media/{self.image}"
    @property
    def show_product(self):
        return reverse("show" , args=[self.id])
    @property
    def delete_product(self):
        return reverse("delete", args=[self.id])
    @property
    def image_url(self):
        return f"/media/{self.img}"



