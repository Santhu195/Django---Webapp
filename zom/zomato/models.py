from django.db import models
from django import forms

# Create your models here.

class cities(models.Model):
    name = models.CharField(max_length =32)
    desc = models.TextField(max_length =32)
    img = models.ImageField(upload_to='pics')
    entity = models.IntegerField()
