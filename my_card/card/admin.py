from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
    fieldsets = [('Datos de la persona', {'fields': ['nombres', 'apellidos', 'telefono','ciudad', 'email', 'mensaje']})]
    list_display = ('nombres', 'apellidos', 'telefono','ciudad', 'email', 'mensaje')
    list_filter = ['nombres']
    search_fields = ['nombres']

admin.site.register(Card, CardAdmin)
# Register your models here.
