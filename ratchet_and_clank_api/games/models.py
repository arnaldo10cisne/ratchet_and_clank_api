from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    # platforms = models.ListField ?

    def __str__(self) -> str:
        return self.name