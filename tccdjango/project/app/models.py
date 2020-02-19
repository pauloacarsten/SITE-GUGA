# Create your models here.
from django.db import models


class UserPerfil (models.Model):
    image = models.ImageField(upload_to='profile_image', blank=True)
