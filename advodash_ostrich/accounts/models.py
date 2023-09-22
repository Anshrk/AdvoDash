from django.contrib.auth.models import AbstractUser
from django.db import models

class Firm(models.Model):
    firm_name = models.CharField(max_length=40)

class Position(models.Model):
    ...
    # Firm owner
    # privillaged users
    # Users
    

# Create your models here.
class FirmUser(AbstractUser):
    email = models.EmailField(unique=True)
    firm = models.ForeignKey(Firm, null=True, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, null=True, on_delete=models.CASCADE)



