from django.contrib import admin
from .models import MjestoUTvornici, Stroj

modeli = [MjestoUTvornici, Stroj]

admin.site.register(modeli)
