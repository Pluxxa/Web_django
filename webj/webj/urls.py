from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),      # Корневой маршрут для приложения main
    path('main_1/', include('main_1.urls'))  # Используем 'main_1/' чтобы избежать конфликтов
]
