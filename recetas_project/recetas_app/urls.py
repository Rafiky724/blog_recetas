from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing, name='landing'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('registro/', views.registro, name='registro'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('receta/nueva/', views.crear_receta, name='crear_receta'),
    path('receta/<int:receta_id>/editar/', views.editar_receta, name='editar_receta'),
    path('receta/<int:receta_id>/eliminar/', views.eliminar_receta, name='eliminar_receta'),
    path('receta/<int:receta_id>/valorar/', views.valorar_receta, name='valorar_receta'),
    
    #
    path('receta/<int:receta_id>/comentario/nuevo/', views.crear_comentario, name='crear_comentario'),
    path('comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)