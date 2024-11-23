from datetime import datetime
from django.db import models
from django.db.utils import IntegrityError
import pandas as pd  # Add this import at the top

from ForexFProject.scraper.webscraping import webscrape  # Import the scraping function

# Main table for webscraping of exchange rates - Rob
class Rates(models.Model):
    currency = models.CharField(max_length=255, null=True, blank=True)  # Full name of the currency
    iso = models.CharField(max_length=3, default='')  # ISO code (e.g., USD, EUR)
    amount = models.IntegerField(default=1)  # Amount (e.g., 1 unit of the currency)
    dev_buy = models.FloatField(default=0.0, null=True, blank=True)  # Development (cashless) buy rate
    dev_sale = models.FloatField(default=0.0, null=True, blank=True)  # Development (cashless) sale rate
    dev_mid = models.FloatField(default=0.0, null=True, blank=True)  # Development (cashless) mid rate
    vault_buy = models.FloatField(default=0.0, null=True, blank=True)  # Vault (cash) buy rate
    vault_sale = models.FloatField(default=0.0, null=True, blank=True)  # Vault (cash) sale rate
    vault_mid = models.FloatField(default=0.0, null=True, blank=True)  # Vault (cash) mid rate
    cnb = models.FloatField(default=0.0, null=True, blank=True)  # Czech National Bank rate
    date = models.DateField(null=True, blank=True)  # Date of the rate
    bank = models.CharField(max_length=255, null=True, blank=True)  # Name of the bank providing the rates

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

# Users table - Rob
class Users(models.Model):
    name = models.CharField(max_length=55)  # Provider Name
    email= models.CharField(max_length=55)  # Type - Bank/Exchange Office/Development

    def __str__(self):
        return f"{self.name}: {self.email}"

# Users table - Rob
class Watchdog_pref(models.Model):
    user_id = models.IntegerField(default=1)  # User Id
    Acc_type= models.CharField(max_length=55)  # Type
    Currency_Iso=models.CharField(max_length=3)
    Buy=models.FloatField(default=0.0, null=True, blank=True)
    Sell = models.FloatField(default=0.0, null=True, blank=True)
    Middle = models.FloatField(default=0.0, null=True, blank=True)
    Value_max = models.FloatField(default=0.0, null=True, blank=True)
    Value_min = models.FloatField(default=0.0, null=True, blank=True)


# Function to scrape and load data to rates - Rob

def update_rates_table(data):
    """
    Updates the Rates table with scraped data, adding only missing records.

    Parameters:
    - data (DataFrame): The pandas DataFrame containing scraped data.
    """
    if data.empty:
        print("No data to update.")
        return

    # Step 1: Ensure data['date'] is in datetime format
    data['date'] = pd.to_datetime(data['date'], format='%d.%m.%Y')

    # Step 2: Iterate through the data and insert only missing records
    for _, row in data.iterrows():
        try:
            # Check if the record already exists (by ISO, date, and bank)
            exists = Rates.objects.filter(
                iso=row['ISO'],
                date=row['date'],
                bank=row['bank']
            ).exists()

            if not exists:
                # Insert the new record
                Rates.objects.create(
                    currency=row['currency'],       # Full currency name
                    iso=row['ISO'],                 # ISO code
                    amount=row['amount'],           # Amount (e.g., 1 unit of the currency)
                    dev_buy=row['dev_buy'],         # Development buy rate
                    dev_sale=row['dev_sell'],       # Development sale rate
                    dev_mid=row['dev_middle'],      # Development mid rate
                    vault_buy=row['vault_buy'],     # Vault (cash) buy rate
                    vault_sale=row['vault_sell'],   # Vault (cash) sale rate
                    vault_mid=row['vault_middle'],  # Vault (cash) mid rate
                    cnb=row['dev_middle'],          # Assume CNB rate matches dev_mid
                    date=row['date'].date(),        # Convert to Python date
                    bank=row['bank']                # Bank name
                )
                print(f"Inserted new rate for ISO: {row['ISO']}, Bank: {row['bank']}, Date: {row['date'].date()}")
            else:
                print(f"Data for ISO: {row['ISO']}, Bank: {row['bank']}, Date: {row['date'].date()} already exists. Skipping.")
        except IntegrityError as e:
            print(f"Error inserting record for ISO: {row['ISO']}, Bank: {row['bank']} - {e}")
