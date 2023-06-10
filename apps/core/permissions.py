import copy
from rest_framework.permissions import DjangoModelPermissions

class CustomDjangoModelPermissions(DjangoModelPermissions):

    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map) 
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['OPTIONS'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['HEAD'] = ['%(app_label)s.view_%(model_name)s']

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True
        
        # Check django.contrib.auth permissions
        if not super().has_permission(request, view): return False

        action = view.action

        # skip as they are part of django.contrib.auth permissions
        if action in ['list', 'create', 'destroy', 'update', 'retrieve']: return True

        # only authenticated users can do OPTIONS and HEAD, DjangoModelPermissions allows authenticated users only already
        if request.method in ['OPTIONS', 'HEAD']: return True

        # check custom view permissions
        app_label = view.get_queryset().model._meta.app_label
        model_name = view.get_queryset().model._meta.model_name
        permission_code = f'{app_label}.{action}_{model_name}'

        return request.user.has_perm(permission_code)
