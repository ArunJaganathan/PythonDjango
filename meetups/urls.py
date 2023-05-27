from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),  #domain/meetups
    path('meetups/',views.index),  #domain/meetups
    path('meetups/login/',views.login),
    path('meetups/widgets/',views.widgets),
    path('meetups/recently-added-products/',views.productdetails),
    path('meetups/latest-Orders/',views.latestOrders),
]