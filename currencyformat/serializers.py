from rest_framework import serializers 
from currencyformat.models import WorldCurrencyFormat
 
class WorldCurrencyFormatSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = WorldCurrencyFormat
        fields = ('id',
                  'name',
                  'country',
                  'currency',
                  'currency_symbol',
                  'currency_code',
                  'currency_thousand_delimeter',
                  'currency_decimal_delimeter',
                  'currency_symbol_ubication',
                  'bool_cents')