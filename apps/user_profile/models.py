from __future__ import unicode_literals
from django.db import models
from ..login_register.models import User, UserManager


class Profile(models.Model):
    user = models.ForeignKey(User, related_name="user_profile")
    birthday = models.DateField(default=False)
    occupation = models.CharField(max_length=255)
    company = models.CharField(max_length=255)

    street_number = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    longtitude = models.IntegerField(default=0)
    latitude = models.IntegerField(default=0)

    about_me = models.CharField(max_length=500)
    distAway = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)

class Image(models.Model):
    user = models.ForeignKey(User, related_name="user_image")
    avatar = models.ImageField(upload_to='login_register/avatar/', default='login_register/avatar/default/default.jpg')
