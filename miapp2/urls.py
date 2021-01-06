"""urls miapp2"""

from django.urls import path
from . import views


urlpatterns = [
    # path para ver html extendido y base
    path("extendido/", views.mostrar_extendido),
    path("base/", views.mostrar_base),
    
    # path para ver html contacto
    path("contacto/", views.contacto),
  
]

