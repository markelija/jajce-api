from django.contrib import admin

from .models import PrijavaKvara, RadniNalog

modeli = [PrijavaKvara, RadniNalog]

admin.site.register(modeli)
