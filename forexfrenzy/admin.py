from django.contrib import admin
from .models import Rates

@admin.register(Rates)
class RateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'iso', 'dev_buy', 'dev_sale', 'vault_cnb')
