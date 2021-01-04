"""urls miapp2"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.mostrar_index2),
    path("index/", views.index),

]

