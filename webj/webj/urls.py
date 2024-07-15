# project_root/urls.py
from django.contrib import admin
from django.urls import path, include
from main_1 import views as main_1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('main_1/', include('main_1.urls')),
    path('', main_1_views.index, name='index'),
]
