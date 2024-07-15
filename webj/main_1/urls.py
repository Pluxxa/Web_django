from django.urls import path
from . import views

urlpatterns = [
    path('', views.data, name='data'),     # Главная страница для main_1
    path('test/', views.test, name='test')  # Страница test для main_1
]
