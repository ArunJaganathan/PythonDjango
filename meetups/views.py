from django.shortcuts import render
#from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Latestorder
from .models import Recentlyaddedproducts
# Create your views here.

def index(request):
    latest_orders = Latestorder.objects.all().order_by('-id')[:5]    
    recent_products = Recentlyaddedproducts.objects.all().order_by('-id')[:5] 

    #paginator = Paginator(latest_orders, per_page=3)   
    #print(latest_orders)
    return render(request,'meetups/index.html',{
        'latest_orders':latest_orders,
        'recent_products':recent_products,
    })

def login(request):
    return render(request,'meetups/login.html')    

def widgets(request):
    return render(request,'meetups/widgets.html')     

def productdetails(request):
    recent_products = Recentlyaddedproducts.objects.all().order_by('-id') 
    return render(request,'meetups/recentlyaddedproducts.html',{
        'recent_products':recent_products,
    })  

def latestOrders(request):
    latest_orders = Latestorder.objects.all().order_by('-id')   
    return render(request,'meetups/latest_orders.html',{
        'latest_orders':latest_orders,
    })     