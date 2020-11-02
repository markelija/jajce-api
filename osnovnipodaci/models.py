from django.db import models

class RadnoMjesto(models.Model):
  
  naziv = models.CharField(max_length=44)

  class Meta(object):
    verbose_name_plural = 'Radna mjesta'

  def __str__(self):
    return self.naziv

class VrstaOdrzavanja(models.Model):
    naziv = models.CharField(max_length=50)

    class Meta(object):
        verbose_name_plural = 'Vrste održavanja'
    def __str__(self):
        return self.naziv
    
class RadnaSmjena(models.Model):
    naziv = models.CharField(max_length=50)

    class Meta(object):
        verbose_name_plural = 'Radne smjene'
    def __str__(self):
        return self.naziv