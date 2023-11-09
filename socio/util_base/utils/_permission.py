'''
THis file contains the logics of 
    - user permission 
    - validate user when they login 
        based on their permission 
'''


from rest_framework.permissions import BasePermission
from django.http import JsonResponse
from accounts.models import User
from util_base.utils._choices import (
    UserRolesChoices,
)



## Will check if the user is an Admin
class IsSocian(BasePermission):
    message = 'User Is Not Socio'
    def has_permission(self, request, view):
        try:
            return bool(request.user.is_authenticated and 
                        request.user.user_role==UserRolesChoices.SOCIAN)
            
        except User.DoesNotExist:
            return JsonResponse({'Error':'Sorry User is not Socian'})