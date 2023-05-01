from django.shortcuts import render
from App.models import Product
from django.http import HttpResponseRedirect
# Create your views here.
# Home
def home(request):
    all_product=Product.objects.all().order_by('-created_at')
    return render(request,'home.html',{"products":all_product})


# add product
def add_product(request):
    if request.method=="POST":
        product=Product()
        product.product=request.POST.get('product')
        product.purchase=request.POST.get('purchase')
        product.sale=request.POST.get('sale')
        product.qty=request.POST.get('qty')
        product.gender=request.POST.get('gender')
        product.note=request.POST.get('note')
        product.save()
        return HttpResponseRedirect('/')
    else:
        return render(request,'add.html')
        
# view the product individually
def product(request,product_id):
    product=Product.objects.get(id=product_id)
    if product!= None:
        return render(request,'edit.html',{'product':product})
# edit product 
def edit_product(request):
    if request.method=="POST":
        product=Product.objects.get(id=request.POST.get('id'))
        if product != None:
            product.product=request.POST.get('product')
            product.purchase=request.POST.get('purchase')
            product.sale=request.POST.get('sale')
            product.qty=request.POST.get('qty')
            product.gender=request.POST.get('gender')
            product.note=request.POST.get('note')
            product.save()
            return HttpResponseRedirect('/')
        

# delete product
def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect('/')