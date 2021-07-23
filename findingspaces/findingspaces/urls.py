from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('vendorbackend.urls')),
    path('', include('buyerbackend.urls')),
]
