from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('producttypes/', views.producttypes, name='types'),
    path('getproducts/', views.getproducts, name='getproducts'),
    path('productdetail/<int:id>', views.productdetail, name='productdetail'),
    path('newProduct/', views.newProduct, name='newproduct'),
]