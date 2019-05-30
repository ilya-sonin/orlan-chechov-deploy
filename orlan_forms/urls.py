from django.urls import path
from . import views

urlpatterns = [
    path('parent_form/', views.parent_form),
    path('contact_form/', views.contact_form),
    path('phone-form/', views.phone_form)
]
