from django.contrib import admin

from .models import RadnaSmjena, VrstaOdrzavanja, RadnoMjesto

modeli = [RadnaSmjena, VrstaOdrzavanja, RadnoMjesto]

admin.site.register(modeli)
