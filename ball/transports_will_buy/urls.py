from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('transports/', views.TransportWillBuyListView.as_view()),
    path('transport/<int:pk>/', views.TransportWillBuyDetailView.as_view()),
]
