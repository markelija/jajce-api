from django.db import models
from strojevi.models import Stroj
from zaposleni.models import Zaposlenik

class PrijavaKvara(models.Model):

  stroj         = models.ForeignKey(Stroj, on_delete=models.CASCADE)
  datum         = models.DateField(null=True)
  opis_kvara    = models.TextField(null=True)


  class Meta(object):
    verbose_name_plural = 'Prijava kvara'

class RadniNalog(models.Model):

  djelatnici = models.ManyToManyField(Zaposlenik)

  class Meta(object):
    verbose_name_plural = 'Radni nalozi'

  def __str__(self):
    return self.test
