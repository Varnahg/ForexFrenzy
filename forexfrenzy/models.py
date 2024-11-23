from django.db import models


# Main table for webscraping of exchange rates - Rob
class Rates(models.Model):
    currency = models.CharField(max_length=255,null=True, blank=True)  # Full name of the currency
    iso = models.CharField(max_length=3,default='')  # ISO code (e.g., USD, EUR)
    amount = models.IntegerField(default=1)  # Amount (e.g., 1 unit of the currency)
    dev_buy = models.FloatField(default=0.0)  # Development (cashless) buy rate
    dev_sale = models.FloatField(default=0.0)  # Development (cashless) sale rate
    dev_mid = models.FloatField(default=0.0)  # Development (cashless) mid rate
    vault_buy = models.FloatField(default=0.0)  # Vault (cash) buy rate
    vault_sale = models.FloatField(default=0.0)  # Vault (cash) sale rate
    vault_mid = models.FloatField(default=0.0)  # Vault (cash) mid rate
    cnb = models.FloatField(default=0.0)  # Czech National Bank rate
    date = models.DateField(null=True, blank=True)  # Corrected the type for date
    bank = models.CharField(max_length=255,null=True, blank=True)  # Name of the bank providing the rates

    def __str__(self):
       return f"{self.currency} ({self.iso}) - {self.bank} on {self.date or 'No Date'}"

# Flag icons table - Rob
class Flags(models.Model):
    iso = models.CharField(max_length=3, unique=True)  # ISO code (e.g., USD, EUR)
    path = models.CharField(max_length=250)  # File path for the flag image

    def __str__(self):
        return f"{self.iso}: {self.path}"


# Provider Type  table - Rob
class Provider(models.Model):
    name = models.CharField(max_length=300, unique=True)  # Provider Name
    type = models.CharField(max_length=15)  # Type - Bank/Exchange Office/Development

    def __str__(self):
        return f"{self.name}: {self.type}"

