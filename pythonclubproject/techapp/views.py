from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product
from .forms import ProductForm

# Create your views here.
def index (request):
    return render(request, 'techapp/index.html')

def producttypes (request):
    type_list = ProductType.objects.all()
    return render(request, 'techapp/types.html', {'type_list': type_list})

def getproducts (request):
    product_list = Product.objects.all()
    return render(request, 'techapp/products.html', {'product_list': product_list})

def productdetail(request, id):
    detail=get_object_or_404(Product, pk=id)
    return render(request, 'techapp/details.html', {'detail' : detail})

#form view
def newProduct(request):
    form=ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = ProductForm()
    else:
        form = ProductForm()
    return render(request, 'techapp/newproduct.html', {'form': form})