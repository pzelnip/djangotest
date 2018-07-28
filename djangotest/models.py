from django.db import models


# Create your models here.
class Counter(models.Model):
    """Model definition for Counter."""

    count = models.IntegerField(default=0)
