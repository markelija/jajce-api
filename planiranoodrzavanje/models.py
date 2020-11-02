from django.db import models
from strojevi.models import Stroj

class PlaniranoOdrzavanje(models.Model):

  stroj         = models.ForeignKey(Stroj, on_delete=models.CASCADE)
  datum         = models.DateTimeField(null=True)
  opis_posla    = models.TextField(null=True)
  vrijeme_rada  = models.TimeField(null=True)


  class Meta(object):
    verbose_name_plural = 'Planirana održavanje'


