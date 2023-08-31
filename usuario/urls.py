from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'usuario'

urlpatterns = [    
    path('nuevo/', login_required(views.NuevoUsuario.as_view()), name='nuevo'),
    path('lista/', login_required(views.UsuariosList.as_view()), name='lista'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('logout/', login_required(views.logout_view), name='logout'),
    path('cambia_grupo/<int:id_gpo>/<int:id_usuario>', login_required(views.cambia_grupo), name='cambia_grupo'),
    
]