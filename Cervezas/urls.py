from django.urls import path
from Cervezas.views import lista_cervezas, crear_cerveza, primer_formulario, buscar_cerveza, borrar_cervezas, actualizar_cerveza,detalle_cervezas


urlpatterns = [
    path('lista-cervezas/', lista_cervezas, name='lista_cervezas'),
    path('crear-cerveza/', crear_cerveza, name='crear_cerveza'),
    path('primer-formulario/', primer_formulario, name='primer_formulario'),
    path('search-cervezas/', buscar_cerveza, name='buscar_cerveza'),
    path('delete-cerveza/<int:pk>/', borrar_cervezas, name='borrar_cervezas'),
    path('update-cerveza/<int:pk>/', actualizar_cerveza, name='actualizar_cerveza'),
    path('detalle-cerveza/<int:pk>/',detalle_cervezas,name='detalle_cerveza')
]