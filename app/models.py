from django.db import models
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField
from django.contrib.gis.db import models as models_gis


# Create your models here.
class Partner(models.Model):
  name = models.CharField(max_length=100, unique=True)
  position = models.PositiveIntegerField()
  image = FilerImageField(help_text='Please supply an image of this partner')
  url = models.CharField('Url', max_length=255, blank=True, null=True, default='#', help_text='Link partner website')
  is_active = models.BooleanField(default=True)
  


  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Partners'


class TeamMember(models.Model):
  name = models.CharField(max_length=255)
  rol = models.CharField(max_length=255)
  description = models.TextField()
  url_profile = models.CharField(max_length=255)
  is_lab_affiliate = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  position = models.DecimalField(max_digits=5, decimal_places=1, default=0, blank=True, null=True, help_text='Position Member')
  image = FilerImageField(help_text='Please supply an image of this partner')


  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Team Members'

class Project(models_gis.Model):
  name = models_gis.CharField(max_length=255)
  description = models_gis.TextField()
  point = models_gis.PointField()
  url = models_gis.CharField(max_length=255, default="#")
  position = models.DecimalField(max_digits=5, decimal_places=1, default=0, blank=True, null=True, help_text='Position Project')
  is_active = models_gis.BooleanField(default=True)
  image1 = FilerImageField(help_text='Please supply an image for this project', related_name="image1_project", blank=True, null=True, default=None)
  image2 = FilerImageField(help_text='Please supply an image for this project', related_name="image2_project", blank=True, null=True, default=None)
  image3 = FilerImageField(help_text='Please supply an image for this project', related_name="image3_project", blank=True, null=True, default=None)
  image4 = FilerImageField(help_text='Please supply an image for this project', related_name="image4_project", blank=True, null=True, default=None)
  image5 = FilerImageField(help_text='Please supply an image for this project', related_name="image5_project", blank=True, null=True, default=None)
  image6 = FilerImageField(help_text='Please supply an image for this project', related_name="image6_project", blank=True, null=True, default=None)
  image7 = FilerImageField(help_text='Please supply an image for this project', related_name="image7_project", blank=True, null=True, default=None)
  image8 = FilerImageField(help_text='Please supply an image for this project', related_name="image8_project", blank=True, null=True, default=None)
  image9 = FilerImageField(help_text='Please supply an image for this project', related_name="image9_project", blank=True, null=True, default=None)
  image10 = FilerImageField(help_text='Please supply an image for this project', related_name="image10_project", blank=True, null=True, default=None)
  
  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Projects'
# class ImageProject(models.Model):
#   image = FilerImageField(help_text='Please supply an image for this project')
#   project = models.ForeignKey(Project)