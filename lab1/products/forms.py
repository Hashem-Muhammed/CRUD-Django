
from django import forms
from products.models import Category , Product

class ProductForm(forms.ModelForm):
    # name = forms.CharField(required=True , label="Product Name")
    # price = forms.IntegerField(required=True , label="Price")
    # img = forms.ImageField(required=False , label="Image" )
    # category = forms.ChoiceField(required=True , choices=Category.get_categories().values_list('id','name'), label="Category")
    class Meta:
        model = Product
        fields = "__all__"