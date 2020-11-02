from django.db import models
from osnovnipodaci.models import RadnoMjesto

class Zaposlenik(models.Model):
  ime = models.CharField(max_length=44, null=True)
  prezime = models.CharField(max_length=44, null=True)
  radno_mjesto = models.ForeignKey(RadnoMjesto, on_delete=models.CASCADE)
  telefon = models.CharField(max_length=15)

  class Meta(object):
    verbose_name_plural = 'Zaposleni'

  def __str__(self):
    return self.ime + ' ' + self.prezime
