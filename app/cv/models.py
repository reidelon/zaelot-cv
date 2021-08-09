from django.db import models

from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'role'


class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'custom_user'
