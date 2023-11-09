## Account & timestamp system 

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from accounts.managers import CustomUserManager
from util_base.utils._choices import UserRolesChoices





class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, blank=True, unique=True, null=True)
    # email = models.EmailField("email_address", unique=True, null=True, blank=True)
    user_role = models.CharField(
        max_length=20,
        null=True,
        choices=UserRolesChoices.choices,
        default=UserRolesChoices.SOCIAN
    )

    password = models.CharField(max_length=1500, null=True)
    confirm_password = models.CharField(max_length=1500, null=True)


    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):

        try:
            if self.socio:
                return self.socio.__str__()
        except :
            return self.username

    class Meta:
        verbose_name_plural = "User"
        indexes = [models.Index(fields=["id", "username"])]




