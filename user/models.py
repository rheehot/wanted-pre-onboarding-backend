from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'
