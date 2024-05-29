from django.db import models

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=25)
  species = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return f'{self.name} ({self.id})'