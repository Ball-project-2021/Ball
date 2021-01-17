from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('transports/', views.TransportAccidListView.as_view()),
    path('transport/<int:pk>/', views.TransportAccidDetailView.as_view()),
]
