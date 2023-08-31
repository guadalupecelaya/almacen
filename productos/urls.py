from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'productos'

urlpatterns = [
    path('lista/', login_required(views.ProductoList.as_view()), name='lista'),
    path('nuevo/', login_required(views.nuevo_producto), name='nuevo'),
    path('editar/<int:pk>', views.ProductoActualizar.as_view(), name='editar'),
    path('eliminar/<int:pk>', views.ProductoDelete.as_view(), name='eliminar'),
    


]
