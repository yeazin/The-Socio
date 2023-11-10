## Custom manager for Users 

from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):
    """custom user email where email is unique.
    We can also pass Full name , email and password here"""

    def create_user(self,  password, **extra_fields):
        
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password,**extra_fields):
        """Create and save Super user with given email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Supperuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Supperuser must have is_superuser=True")

        return self.create_user( password,**extra_fields)
