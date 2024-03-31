from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from math import ceil

# Create your views here.
def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render('request','shop/index.html')
    # return HttpResponse("Index Shop")

def about(request):
    return render('request','shop/about.html')
    # return HttpResponse("about")

def contact(request):
    return HttpResponse("Contact")

def tracker(request):
    return HttpResponse("Tracker")

def search(request):
    return HttpResponse("search")

def prodview(request):
    return HttpResponse("Product view")

def checkout(request):
    return HttpResponse("Checkout")