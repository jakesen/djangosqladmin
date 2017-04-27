from django.db import models
from django.contrib.auth.models import User

class Database(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    port = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.title
