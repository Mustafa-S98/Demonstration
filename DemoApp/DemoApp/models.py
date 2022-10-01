import imp
from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 20)
    pwd = models.CharField(max_length = 16)