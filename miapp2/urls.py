"""urls miapp2"""

from django.urls import path
from . import views


urlpatterns = [
    path("extendido/", views.mostrar_extendido),
    path("base/", views.mostrar_base),
    path("contacto/", views.contacto),
  
]

