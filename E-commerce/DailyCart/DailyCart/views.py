from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Blog Index")
def index(request):
    return render(request,'shop/index1.html')

def shop(request):
    return render(request,'shop/index.html')