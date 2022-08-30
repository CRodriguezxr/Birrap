from django.contrib import admin
from Comidas.models import Comidas

@admin.register(Comidas)
class Comidas_admin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
# Register your models here.