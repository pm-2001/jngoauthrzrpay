from django.contrib import admin
from django.urls import path
from pay import views

urlpatterns = [
    path('', views.home)
]
