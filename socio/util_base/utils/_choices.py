"""

NWU choices models 

"""
from django.db import models


class UserRolesChoices(models.TextChoices):

    SOCIAN      = 'socian', 'Socian'
    ADMIN       = 'admin', 'Admin'