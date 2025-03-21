from django.db import models
from django.utils import timezone


class Personal(models.Model):
    # personal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name

class Roles(models.Model):
    # personal_role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30)
    # personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    personal = models.ManyToManyField(Personal, related_name='roles')

    def __str__(self):
        return self.role

