from django.urls import path
from . import views

urlpatterns = [
    path('profiledetails/', views.profileDetails, name='profiledetails'),
]
