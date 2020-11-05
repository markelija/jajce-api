from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.AdminSite.site_header = 'Jajce Alloy Wheels'
admin.AdminSite.index_title = 'Administracija'
admin.AdminSite.site_title = 'JAW'
