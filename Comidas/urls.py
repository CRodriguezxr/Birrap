from django.urls import path
from Comidas.views import lista_comidas, crear_comida, primer_formulario, buscar_comida, borrar_comida, actualizar_comidas, detalle_comidas


urlpatterns = [
    path('lista-comidas/', lista_comidas, name='lista_comidas'),
    path('crear-comidas/', crear_comida, name='crear_comidas'),
    path('primer-formulario/', primer_formulario, name='primer_formulario'),
    path('search-comidas/', buscar_comida, name='buscar_comidas'),
    path('delete-comidas/<int:pk>/', borrar_comida, name='borrar_comidas'),
    path('update-comidas/<int:pk>/', actualizar_comidas, name='actualizar_comidas'),
    path('detalle-comidas/<int:pk>/',detalle_comidas, name='detalle_comidas')
]