from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone=models.CharField(max_length=11,unique=True)

    class Meta:
        db_table='user'

