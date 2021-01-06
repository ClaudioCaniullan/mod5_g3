"""urls miapp2"""

from django.urls import path
from . import views


urlpatterns = [
    # path para ver html extendido y base
    path("extendido/", views.mostrar_extendido),
    path("base/", views.mostrar_base),
    
    # path de pruebas para ver formulario contacto y contador de palabras
    path("contacto/", views.contacto),
    path("palabras/", views.contador_palabras),
  
]

