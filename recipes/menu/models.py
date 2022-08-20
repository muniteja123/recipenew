from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    ingrediants = models.TextField(max_length=200)
    process = models.TextField(max_length=200)

    def __str__(self):
        return self.name