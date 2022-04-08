from django.db import models
from django.contrib.auth.models import AbstractUser

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    paid_until = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Client(AbstractUser):
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT, null=True, blank=True)

class Tenant(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    subdomain = models.CharField(max_length=100)
    database = models.CharField(max_length=200)
    schema = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name