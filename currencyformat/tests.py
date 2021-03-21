from django.test import TestCase
from datetime import date, timedelta
from .models import WorldCurrencyFormat
from collections import OrderedDict
from currencyformat.utils import *
import json

# Create your tests here.
class WorldCurrencyFormatTest(TestCase):

    def setUp(self):
        self.worldcurrencyformat = WorldCurrencyFormat.objects.create(
            name = 'Ecuadorian Dollar',
            country = "Ecuador",
            currency = "USD",
            currency_symbol="$",
            currency_code="USD",
            currency_thousand_delimeter=".",
            currency_decimal_delimeter=",",
            currency_symbol_ubication="left",
            display_currency="symbol",
            bool_cents=True,
        )
        self.worldcurrencyformat.save()
        self.format_currency = returnFormatCurrency(self.worldcurrencyformat.currency_symbol, self.worldcurrencyformat.currency_code, self.worldcurrencyformat.currency_thousand_delimeter, self.worldcurrencyformat.currency_decimal_delimeter, self.worldcurrencyformat.currency_symbol_ubication, self.worldcurrencyformat.display_currency, self.worldcurrencyformat.bool_cents)

    def test_read_worldcurrencyformat(self):
        self.assertEqual(self.worldcurrencyformat.country, 'Ecuador')
        self.assertEqual(self.worldcurrencyformat.currency, 'USD')
        self.assertEqual(self.format_currency, '$#.###,##')

    def test_update_task_description(self):
        self.worldcurrencyformat.currency_thousand_delimeter = ','
        self.worldcurrencyformat.currency_decimal_delimeter = '.'
        self.worldcurrencyformat.save()
        self.format_currency = returnFormatCurrency(self.worldcurrencyformat.currency_symbol, self.worldcurrencyformat.currency_code, self.worldcurrencyformat.currency_thousand_delimeter, self.worldcurrencyformat.currency_decimal_delimeter, self.worldcurrencyformat.currency_symbol_ubication, self.worldcurrencyformat.display_currency, self.worldcurrencyformat.bool_cents)

        self.assertEqual(self.format_currency, '$#,###.##')

class WorldCurrencyFormatAPITest(TestCase):

    def setUp(self):
        self.client.login(username='', password='')

    def test_one_worldcurrencyformat_getById(self):
        data_created =  {
                            "name": "Ecuadorian Dollar",
                            "country": "Ecuador",
                            "currency": "USD",
                            "currency_symbol_ubication": "left",
                            "currency_code": "USD",
                            "currency_symbol": "$",
                            "currency_thousand_delimeter": ".",
                            "currency_decimal_delimeter": ",",
                            "display_currency": "symbol",
                            "bool_cents": "True"
                        }
        response1 = self.client.post('/api/v1/worldcurrencyformat/create', data_created)
        self.assertEqual(response1.status_code, 200)

        response = self.client.get('/api/v1/worldcurrencyformat/1')
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data, {   
                                            "message": "$#.###,##",
                                            "status": "Success"
                                        }
                        )
    
    def test_two_worldcurrencyformat_read(self):
        self.worldcurrencyformat = WorldCurrencyFormat.objects.create(
            name = 'Spain Euro',
            country = "Spain",
            currency = "EUR",
            currency_symbol="€",
            currency_code="EUR",
            currency_thousand_delimeter=",",
            currency_decimal_delimeter=".",
            currency_symbol_ubication="right",
            display_currency="symbol",
            bool_cents=False,
        )
        self.worldcurrencyformat.save()

        response = self.client.post('/api/v1/worldcurrencyformat/', {'country': 'Spain', 'currency': 'EUR'})
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data, {"message": "#,###€", "status": "Success"})

        response = self.client.post('/api/v1/worldcurrencyformat/test', {'country': 'Spain', 'currency': 'EUR', 'price': '2.000,00'})
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data, {"message": "2,000€", "status": "Success"})

    def test_three_worldcurrencyformat_create_and_delete(self):
        data_created =  {
                            "name": "Argentina - Pesos",
                            "country": "Argentina",
                            "currency": "USD",
                            "currency_symbol_ubication": "left",
                            "currency_code": "USD",
                            "currency_symbol": "ASR",
                            "currency_thousand_delimeter": ".",
                            "currency_decimal_delimeter": ",",
                            "display_currency": "code",
                            "bool_cents": "False"
                        }
        response1 = self.client.post('/api/v1/worldcurrencyformat/create', data_created)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.data, {"message": "Element USD-Argentina created." , "status": "Success"})

        response = self.client.post('/api/v1/worldcurrencyformat/delete', {'country': 'Argentina', 'currency': 'USD'})
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data, {"message": "Element USD-Argentina deleted." , "status": "Success"})