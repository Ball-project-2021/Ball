from django.contrib import admin
from django.urls import path, include
from .views import TransportsView

urlpatterns = [
    path('all', TransportsView.as_view())
]
