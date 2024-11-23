from django.db import models

# Main table for webscrapping of exchange rates - Rob
class Rates(models.Model):
    currency = models.CharField(max_length=255)
    iso = models.CharField(max_length=3)
    dev_buy = models.FloatField()
    dev_sale = models.FloatField()
    dev_mid = models.FloatField()
    vault_buy = models.FloatField()
    vault_sale = models.FloatField()
    vault_cnb = models.FloatField()

    def __str__(self):
        return f"{self.currency} ({self.iso})"
