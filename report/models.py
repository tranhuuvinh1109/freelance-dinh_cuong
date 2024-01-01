from django.db import models

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(
        max_length=255, unique=True, default='default username')
    email = models.EmailField(max_length=255, unique=True)
    is_verified = models.BooleanField(default=False)
    avatar = models.CharField(max_length=1000)
    otp = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Reported(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    date_report = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    cable = models.CharField(max_length=20)
    power = models.CharField(max_length=255)
    report = models.CharField(max_length=20000)
    other_job = models.CharField(max_length=20000)
    exist = models.CharField(max_length=20000)
    propose = models.CharField(max_length=20000)
    creator = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    sv_device = models.CharField(max_length=255)
    sv_cable = models.CharField(max_length=255)
    sv_power = models.CharField(max_length=255)

