from django.db import models

# Create your models here.
class WorldCurrencyFormat(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=False)
    currency = models.CharField(max_length=100, blank=False)
    currency_symbol = models.CharField(max_length=30)
    currency_code = models.CharField(max_length=30)
    currency_thousand_delimeter = models.CharField(max_length=2, default=".")
    currency_decimal_delimeter = models.CharField(max_length=2, default=",")
    currency_symbol_ubication = models.CharField(max_length=10, default="left")
    display_currency = models.CharField(max_length=10, default="symbol")
    bool_cents = models.BooleanField(default=False)

    def __str__(self):
        return self.country + " " + self.currency