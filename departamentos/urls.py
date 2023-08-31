from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'departamentos'

urlpatterns = [
    path('lista/', login_required(views.DepartamentoList.as_view()), name='lista'),
    path('nuevo/', login_required(views.DepartamentoCrear.as_view()), name='nuevo'),
    path('eliminar/<int:pk>', views.DepartamentoDelete.as_view(), name='eliminar'),

]