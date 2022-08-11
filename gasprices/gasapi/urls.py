from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('houston/', views.houston, name='houston')
]