from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("", views.incio, name="inicio"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("libros", views.libros, name="libros"),
    path("libros/crear", views.crear_libro, name="crear-libro"),
    # path("libros/editar", views.editar_libro, name="editar-libro"),
    path("libros/editar/<int:id>", views.editar_libro, name="editar-libro"),
    path("libros/eliminar/<int:id>", views.eliminar_libro, name="eliminar-libro"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
