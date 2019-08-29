from django.urls import path

from . import views

urlpatterns = [
    path('recive/', views.recive),
]
