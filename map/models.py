from django.db import models
from django.contrib.gis.db import models as models_gis

# Create your models here.

class Project(models_gis.Model):
  name = models_gis.TextField()
  description = models_gis.TextField()
  point = models_gis.PointField()

  def __str__(self):
    return self.name

class Image(models.Model):
  image = models.ImageField()
  project = models.ForeignKey(Project)