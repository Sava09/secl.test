from django.db import models


# Create your models here.

class ListObject(models.Model):
    name = models.CharField(max_length=20, unique=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
