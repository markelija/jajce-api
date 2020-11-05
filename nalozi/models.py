from django.db import models
from strojevi.models import Stroj
from zaposleni.models import Zaposlenik
from skladiste.models import RezervniDio
from osnovnipodaci.models import VrstaOdrzavanja

class PrijavaKvara(models.Model):

  stroj         = models.ForeignKey(Stroj, on_delete=models.CASCADE)
  datum         = models.DateField(null=True)
  opis_kvara    = models.TextField(null=True)


  class Meta(object):
    verbose_name_plural = 'Prijava kvara'
  
  def __str__(self):
    return self.stroj.naziv


class RadniNalog(models.Model):
  kvar = models.ForeignKey(PrijavaKvara, on_delete=models.CASCADE, null=True, blank=True)
  vrsta_odrzavanja = models.ForeignKey(VrstaOdrzavanja, on_delete=models.CASCADE, null=True)
  djelatnici = models.ManyToManyField(Zaposlenik, null=True)
  opis_posla = models.TextField(null=True)
  pocetak_rada = models.DateTimeField(null=True)
  kraj_rada = models.DateTimeField(null=True)
  rezervni_dijelovi = models.ManyToManyField(RezervniDio, null=True)
  datum = models.DateTimeField(auto_now=True)

  class Meta(object):
    verbose_name_plural = 'Radni nalozi'

