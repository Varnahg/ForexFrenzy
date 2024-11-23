from forexfrenzy.models import Rates

# Add sample data
Rates.objects.create(
    currency="United States Dollar",
    iso="USD",
    dev_buy=23.705,
    dev_sale=25.021,
    dev_mid=24.363,
    vault_buy=23.705,
    vault_sale=25.021,
    vault_cnb=24.337
)

Rates.objects.create(
    currency="Australian Dollar",
    iso="AUD",
    dev_buy=15.406,
    dev_sale=16.262,
    dev_mid=15.834,
    vault_buy=15.406,
    vault_sale=16.262,
    vault_cnb=15.825
)