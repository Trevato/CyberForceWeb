from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """User profile.  Contains some basic configurable settings"""
    user = models.ForeignKey(User, unique=True)
    email = models.CharField(max_length=256, blank=True, default='')
