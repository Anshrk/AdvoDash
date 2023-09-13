from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        ...


class Firm(models.Model):
    firm_name = models.CharField(max_length=40)


class Position(models.Model):
    position = models.CharField(max_length=40)

# Create your models here.
class FirmUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    firm = models.ForeignKey(Firm, null=True, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, null=True, on_delete=models.CASCADE)

