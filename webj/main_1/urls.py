# main_1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
    path('new/', views.new, name='new'),  # добавьте этот путь
]
