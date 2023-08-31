from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'proveedores'

urlpatterns = [
    path('lista/', login_required(views.ProveedorList.as_view()), name='lista'),
    path('nuevo/', login_required(views.ProveedorCrear.as_view()), name='nuevo'),
    path('ver/<int:pk>', views.ProveedorDetalle.as_view(), name='ver'),
    path('editar/<int:pk>', views.ProveedorActualizar.as_view(), name='editar'),
    path('eliminar/<int:pk>', views.ProveedorDelete.as_view(), name='eliminar'),
]
