from django.shortcuts import redirect
from django.contrib.auth.models import Group

def group_names(group:Group):
    return group.name

# Verificar si ese usuario pertenece a ese grupo
def verify_group(usuario, allowed_groups):
    for i in list(usuario.groups.all()):
        if i.name in allowed_groups:
            return True
    return False


def admin_required(function):
    def wrap(request, *args, **kwargs):
        grupos = ["Administración","Administrador Trámites"]
        
        if not verify_group(request.user, grupos):
            return redirect('Inicio')
        return function(request, *args, **kwargs)
    return wrap

def administracion_required(function):
    def wrap(request, *args, **kwargs):
        grupos = ["Administrador de Módulo", "Gestor General SD"]
        
        if not verify_group(request.user, grupos):
            return redirect('Inicio')
        return function(request, *args, **kwargs)
    return wrap

def gestores_tramites_required(function):
    def wrap(request, *args, **kwargs):
        grupos = ["Gestores de Trámites Posgrado","Gestores de Trámites Pregrado","Gestor General SD"]
        
        if not verify_group(request.user, grupos):
            return redirect('Inicio')
        return function(request, *args, **kwargs)
    return wrap

def all_required(function):
    def wrap(request, *args, **kwargs):
        grupos = ["Gestores de Trámites Posgrado","Gestores de Trámites Pregrado","Administrador de Módulo", "Gestor General SD"]
        
        if not verify_group(request.user, grupos):
            return redirect('Inicio')
        return function(request, *args, **kwargs)
    return wrap