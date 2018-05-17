from django.shortcuts import render

# Create your views here.
def checkout(request):
    return render(request, "ds_product/checkout.html")

def detail(request):
    return render(request, "ds_product/detail.html")

def product(request):
    return render(request, "ds_product/product.html")