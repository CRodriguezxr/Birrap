from django.contrib import admin
from Cervezas.models import Cerveza

@admin.register(Cerveza)
class Cervezas_admin(admin.ModelAdmin):
    list_display = ['style', 'description', 'alcohol_volume', 'IBU', 'price']
# Register your models here.
