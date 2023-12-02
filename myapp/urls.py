from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profit/',views.profit_view, name='profit'),
]