from django.db import models

# Create your models here.

from django.db import models


class File(models.Model):
    location = models.CharField(max_length=255, default="NULL")
    tag = models.CharField(max_length=255)
    accessId = models.CharField(max_length=255, default="a")

    class Meta:
        db_table = 'Files'


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default='no-email@example.com')
    join_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'User'
