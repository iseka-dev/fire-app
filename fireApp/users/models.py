from django.db import models
from django.contrib.auth.models import User
from fireMap.models import Cuartel


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='userprofile',
        on_delete=models.CASCADE
    )
    cuartel = models.ForeignKey(
        Cuartel,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
