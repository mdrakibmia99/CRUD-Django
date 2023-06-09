"""CRUD_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('',views.home,name="home"),
    # add product
    path('add_product',views.add_product,name="add_product"),
    # view the product individually
    path('product/<str:product_id>',views.product,name="product"),
    # edit product
    path('edit_product',views.edit_product,name="edit_product"),
    # delete product
    path('delete_product/<str:delete_product',views.delete_product,name="delete_product"),
]
