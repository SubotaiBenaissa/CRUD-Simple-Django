from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('libros/', views.libros, name="libros"),
    path('crear/', views.crearLibro, name="crear"),
    path('editar/', views.editarLibro, name="editar"),
    path('eliminar/<int:id>', views.eliminarLibro, name="eliminar"),
    path('editar/<int:id>', views.editarLibro, name="editar")

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)