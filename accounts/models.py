from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
