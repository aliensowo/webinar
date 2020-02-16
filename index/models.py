from django.db import models

# Create your models here.


class broadcasters(models.Model):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)


class viewer(models.Model):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
