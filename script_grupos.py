from usuario.models import Usuario
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group, User
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'almacenieez.settings')
django.setup()


def crear_grupos():
    administrador_grupo = Group.objects.create(name='admin_grupo')
    manager_grupo = Group.objects.create(name='manager_grupo')
    invitado_grupo = Group.objects.create(name='invitado_grupo')
    print('Crea los grupos') 

    content_type = ContentType.objects.get_for_model(Usuario)
    content_type2 = ContentType.objects.get_for_model(User)

    print('asigna content type')

    
    print('asigna permisos a grupos por content type')

    manager_permiso = Permission.objects.create(
        codename='manager_permiso',
        name='Permiso requerido para managers',
        content_type=content_type
    ) 
    invitado_permiso = Permission.objects.create(
        codename='invitado_permiso',
        name='Permiso requerido para invitados',
        content_type=content_type
    )
    administrador_permiso = Permission.objects.create(
        codename='administrador_permiso',
        name='Permiso requerido para administradores',
        content_type=content_type2
    )

    '''
    administrador_permiso = Permission.objects.get(codename='administrador_permiso')
    manager_grupo = Permission.objects.get(codename='manager_permiso')
    invitado_permiso = Permission.objects.get(codename='invitado_permiso')
   '''

    administrador_grupo.permissions.add(administrador_permiso)
    administrador_grupo.permissions.add(manager_permiso)
    administrador_grupo.permissions.add(invitado_permiso)

    manager_grupo.permissions.add(manager_permiso)
    manager_grupo.permissions.add(invitado_permiso)

    invitado_grupo.permissions.add(invitado_permiso)

    print('Crea los grupos')

    administrador = Usuario.objects.create(first_name='ieez admin',
                                           username='administrador',
                                           rfc='IEE970215TU3')

    manager = Usuario.objects.create(first_name='ieez manager',
                                           username='manager',
                                           rfc='IEE970215TU2')

    invitado = Usuario.objects.create(first_name='ieez invitado',
                                    username='invitado',
                                    rfc='IEE970215TU1')
    print('Crea los usuarios')

    
    administrador.set_password('administrador')
    manager.set_password('manager')
    invitado.set_password('invitado')

  

  
    administrador.save()
    manager.save()
    invitado.save()
    

    administrador_grupo.user_set.add(administrador)
    manager_grupo.user_set.add(manager)
    invitado_grupo.user_set.add(invitado)


    


    
crear_grupos()
