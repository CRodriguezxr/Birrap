from django.contrib import admin
from django.urls import path
from Birrap.views import saludo, segundo_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name = 'saludo'),
    path('Home/', segundo_template, name = 'segundo_template'),
]
