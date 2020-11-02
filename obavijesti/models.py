from django.db import models
from django.contrib.auth.models import User

class Obavijest(models.Model):
    
    autor   = models.ForeignKey(User, on_delete=models.CASCADE)
    naslov  = models.CharField(max_length=50)
    sadrzaj = models.TextField()
    datum   = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name_plural = 'Obavijesti'

    def __str__(self):
        return self.naslov
