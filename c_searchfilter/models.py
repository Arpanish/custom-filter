from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=55)
    address = models.CharField(max_length=55)
