from django.db import models


class MjestoUTvornici(models.Model):
  naziv = models.CharField(max_length=50)

  class Meta(object):
    verbose_name_plural = 'Mjesta u tvornici'
  
  def __str__(self):
    return self.naziv

class Stroj(models.Model):
    naziv = models.CharField(max_length=50)
    mjesto = models.ForeignKey(MjestoUTvornici, on_delete=models.CASCADE)
  
    class Meta(object):
        verbose_name_plural = 'Strojevi'
    
    def __str__(self):
        return self.naziv

