from django.shortcuts import render
from App.models import Product
from django.http import HttpResponseRedirect
# Create your views here.
# Home
def home(request):
    all_product=Product.objects.all().order_by('-created_at')
    return render(request,'home.html',{"products":all_product})

# add product

# view the product individually

# delete product