from django.http import HttpResponse
from django.shortcuts import render
from .models import products


# Create your views here.

def index(request):
    display_products = products.objects.all()
    return render(request, 'index.html', {'display_products': display_products})
