from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(User):
    rfc = models.CharField(
        'RFC',
        max_length=20,
        null=True,
        blank=False)