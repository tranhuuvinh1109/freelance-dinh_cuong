from django.db import models

class Media(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    name_ttcq = models.CharField(max_length=255)
    phone_staff = models.CharField(max_length=20)
    km = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    date = models.CharField(max_length=255)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=2000)

