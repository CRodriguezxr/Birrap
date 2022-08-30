from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from Birrap.views import Saludo, Home, index

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),    

    path('saludo/', Saludo, name = 'saludo'),
    path('Home/', Home, name = 'Home'),

    path('Cervezas/', include('Cervezas.urls')),
    path('Comidas/', include('Comidas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
