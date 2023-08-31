from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'tipoproducto'

urlpatterns = [
    path('lista/', login_required(views.lista_tipoproducto), name='lista'),
    path('eliminar/<int:id>', views.eliminar_tipoproducto, name='eliminar'),
    path('alta/', login_required(views.nuevo_tipoproducto), name='alta'),
    path('editar/<int:id>', views.editar_tipoproducto, name='editar'),
    
]
