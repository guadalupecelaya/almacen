from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'solicitudes'

urlpatterns = [
    path('lista/', login_required(views.SolicitudList.as_view()), name='lista'),
    path('nuevo/', login_required(views.solicitud_nueva), name='nuevo'),
    path('aceptar/<int:id>', views.aceptar_solicitud, name='aceptar'),
    
    
]