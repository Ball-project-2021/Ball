from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('transports/', views.TransportListView.as_view()),
    path('transport/<int:pk>/', views.TransportDetailView.as_view()),
]
