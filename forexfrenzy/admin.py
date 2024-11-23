from django.contrib import admin
from .models import Rates

@admin.register(Rates)
class RateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'iso', 'amount', 'dev_buy', 'dev_sale','date', 'vault_mid', 'bank')
