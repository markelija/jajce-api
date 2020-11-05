from django.contrib import admin

from .models import PrijavaKvara, RadniNalog, RadniNalog

class PrijavaKvaraModelAdmin(admin.ModelAdmin):
    list_display = ['stroj', 'datum']
    search_fields = ['opis_kvara']
    list_filter = ['datum']
    class Meta:
        model = PrijavaKvara

class RadniNalogModelAdmin(admin.ModelAdmin):
    list_display = ['kvar', 'datum']
    list_filter = ['datum']
    search_fields = ['kvar']
    class Meta:
        model = RadniNalog

admin.site.register(PrijavaKvara, PrijavaKvaraModelAdmin)
admin.site.register(RadniNalog, RadniNalogModelAdmin)
