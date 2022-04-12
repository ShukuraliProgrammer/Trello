from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from Common.models import BaseModel


class User(AbstractUser):
    surname = models.CharField(_('Surname'), max_length=150, null=True, blank=True)
    age = models.PositiveIntegerField(_('Age'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
