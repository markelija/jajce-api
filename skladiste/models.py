from django.db import models

class RezervniDio(models.Model):
  naziv       = models.CharField(max_length=50)
  specifikacije = models.CharField(max_length=200, null=True)
  proizvodjac = models.CharField(max_length=50, null=True)
  opis        = models.TextField()
  cijena      = models.DecimalField(max_digits=12, decimal_places=2)

  class Meta(object):
    verbose_name_plural = 'Rezervni dijelovi'
  
  def __str__(self):
    return self.naziv



