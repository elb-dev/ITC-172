from django.shortcuts import render
from .models import ProductType

# Create your views here.
def index (request):
    return render(request, 'techapp/index.html')

def producttypes (request):
    product_list = ProductType.objects.all
    return render(request, 'techapp/types.html', {'product_list': product_list})