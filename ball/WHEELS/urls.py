from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('wheel/', views.WheelListView.as_view()),
    path('wheel/<int:pk>/', views.WheelDetailView.as_view()),
]
