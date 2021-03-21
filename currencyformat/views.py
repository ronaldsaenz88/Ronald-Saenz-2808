from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from currencyformat.models import WorldCurrencyFormat
from currencyformat.serializers import WorldCurrencyFormatSerializer
from rest_framework.decorators import api_view
from currencyformat.utils import *
import json

# Create your views here.

@api_view(['GET'])
def worldcurrencyformat_detail(request, id):
    # find tutorial by pk (id)
    try: 
        worldcurrency = WorldCurrencyFormat.objects.get(id=id) 
        
        format_currency = returnFormatCurrency(worldcurrency.currency_symbol, worldcurrency.currency_code, worldcurrency.currency_thousand_delimeter, worldcurrency.currency_decimal_delimeter, worldcurrency.currency_symbol_ubication, worldcurrency.display_currency, worldcurrency.bool_cents)

        dataWCF = {
            "name": worldcurrency.name,
            "country": worldcurrency.country,
            "currency": worldcurrency.currency,
            "currency_symbol": worldcurrency.currency_symbol,
            "currency_code": worldcurrency.currency_code,
            "currency_thousand_delimeter": worldcurrency.currency_thousand_delimeter,
            "currency_decimal_delimeter": worldcurrency.currency_decimal_delimeter,
            "currency_symbol_ubication": worldcurrency.currency_symbol_ubication,
            "bool_cents": worldcurrency.bool_cents,
            "display_currency": worldcurrency.display_currency,
            "format": format_currency,
        }

        return Response({"message": str(format_currency), "status": "Success"})

    except WorldCurrencyFormat.DoesNotExist: 
        return Response({"message": 'The WorldCurrency does not exist', "status": "Error"})
        #return JsonResponse({'message': 'The WorldCurrency does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
@api_view(['POST'])
def worldcurrencyformat_create(request):
    try:
        body = request.data
        country = body['country'] if 'country' in body else ""
        currency = body['currency'] if 'currency' in body else ""

        worldcurrencies = WorldCurrencyFormat.objects.filter(country=country, currency=currency)
        if worldcurrencies:
            for worldcurrency in worldcurrencies:
                body['currency_symbol'] = body['currency_symbol'] if 'currency_symbol' in body else worldcurrency.currency_symbol
                body['currency_code'] = body['currency_code'] if 'currency_code' in body else worldcurrency.currency_code
                body['name'] = body['name'] if 'name' in body else worldcurrency.name
                body['bool_cents'] = bool(body['bool_cents']) if 'bool_cents' in body else True

                worldcurrency_serializer = WorldCurrencyFormatSerializer(worldcurrency, data=body)
                if worldcurrency_serializer.is_valid():
                    worldcurrency_serializer.save()
                else:
                    print(worldcurrency_serializer.errors)

            return Response({"message": str("Element " +  currency + "-" + country) + " updated.",  "status": "Success"})
        else:
            if "country" in body and "currency" in body and "name" in body and "currency_symbol" in body and "currency_code" in body:
                
                name = body['name'] if 'name' in body else ""
                currency_symbol = body['currency_symbol'] if 'currency_symbol' in body else ""
                currency_code = body['currency_code'] if 'currency_code' in body else ""
                currency_thousand_delimeter = body['currency_thousand_delimeter'] if 'currency_thousand_delimeter' in body else "."
                currency_decimal_delimeter = body['currency_decimal_delimeter'] if 'currency_decimal_delimeter' in body else ","
                currency_symbol_ubication = body['currency_symbol_ubication'] if 'namcurrency_symbol_ubicatione' in body else "left"
                display_currency = body['display_currency'] if 'display_currency' in body else "symbol"
                bool_cents = body['bool_cents'] if 'bool_cents' in body else False


                WorldCurrencyFormat_object = WorldCurrencyFormat.objects.create(
                    name = name,
                    country = country,
                    currency = currency,
                    currency_symbol=currency_symbol,
                    currency_code=currency_code,
                    currency_thousand_delimeter=currency_thousand_delimeter,
                    currency_decimal_delimeter=currency_decimal_delimeter,
                    currency_symbol_ubication=currency_symbol_ubication,
                    display_currency=display_currency,
                    bool_cents=bool_cents,
                )

                worldcurrency_serializer = WorldCurrencyFormatSerializer(WorldCurrencyFormat_object, data=body)
                if worldcurrency_serializer.is_valid():
                    worldcurrency_serializer.save()
                else:
                    print(worldcurrency_serializer.errors)

                return Response({"message": str("Element " +  currency + "-" + country) + " created.",  "status": "Success"})
            else:
                return Response({"message": "WorldCurrencyFormat didn't create, because missing parameters.", "status": "Error"})

    except Exception as e:
        print("Errors:", str(e))
        return Response({"message": "WorldCurrencyFormat does not exist", "status": "Error"})

@api_view(['PUT', 'POST'])
def worldcurrencyformat_update(request):
    try:
        body = request.data
        country = body['country'] if 'country' in body else ""
        currency = body['currency'] if 'currency' in body else ""
        
        worldcurrencies = WorldCurrencyFormat.objects.filter(country=country, currency=currency)
        if worldcurrencies:
            for worldcurrency in worldcurrencies:
                body['currency_symbol'] = body['currency_symbol'] if 'currency_symbol' in body else worldcurrency.currency_symbol
                body['currency_code'] = body['currency_code'] if 'currency_code' in body else worldcurrency.currency_code
                body['name'] = body['name'] if 'name' in body else worldcurrency.name
                body['bool_cents'] = bool(body['bool_cents']) if 'bool_cents' in body else True

                worldcurrency_serializer = WorldCurrencyFormatSerializer(worldcurrency, data=body)
                if worldcurrency_serializer.is_valid():
                    worldcurrency_serializer.save()
                else:
                    print(worldcurrency_serializer.errors)

            return Response({"message": str("Element " +  currency + "-" + country) + " updated.",  "status": "Success"})
        else:
            return Response({"message": "WorldCurrencyFormat does not exist", "status": "Error"})

    except Exception as e:
        print("Errors:", str(e))
        return Response({"message": "WorldCurrencyFormat does not exist", "status": "Error"})

@api_view(['DELETE', 'POST'])
def worldcurrencyformat_delete(request):
    try:
        body = request.data
        country = body['country'] if 'country' in body else ""
        currency = body['currency'] if 'currency' in body else ""

        worldcurrencies = WorldCurrencyFormat.objects.filter(country=country, currency=currency)
        if worldcurrencies:
            for worldcurrency in worldcurrencies:
                worldcurrency.delete()

            return Response({"message": str("Element " +  currency + "-" + country) + " deleted.",  "status": "Success"})
        else:
            print("Errors: adfafasdf")
            print(country, currency)
            return Response({"message": "WorldCurrencyFormat does not exist", "status": "Error"})

    except Exception as e:
        print("Errors:", str(e))
        return Response({"message": "WorldCurrencyFormat does not exist", "status": "Error"})
    
@api_view(['POST'])
def worldcurrencyformat_read(request):
    try:
        body = request.data
        country = body['country'] if 'country' in body else ""
        currency = body['currency'] if 'currency' in body else ""

        worldcurrencies = WorldCurrencyFormat.objects.filter(country=country, currency=currency)
        if worldcurrencies:
            worldcurrency = worldcurrencies[0]
            format_currency = returnFormatCurrency(worldcurrency.currency_symbol, worldcurrency.currency_code, worldcurrency.currency_thousand_delimeter, worldcurrency.currency_decimal_delimeter, worldcurrency.currency_symbol_ubication, worldcurrency.display_currency, worldcurrency.bool_cents)

            dataWCF = {
                "name": worldcurrency.name,
                "country": worldcurrency.country,
                "currency": worldcurrency.currency,
                "currency_symbol": worldcurrency.currency_symbol,
                "currency_code": worldcurrency.currency_code,
                "currency_thousand_delimeter": worldcurrency.currency_thousand_delimeter,
                "currency_decimal_delimeter": worldcurrency.currency_decimal_delimeter,
                "currency_symbol_ubication": worldcurrency.currency_symbol_ubication,
                "bool_cents": worldcurrency.bool_cents,
                "display_currency": worldcurrency.display_currency,
                "format": format_currency,
            }

            return Response({"message": str(format_currency), "status": "Success"})
        else:
            return Response({"message": 'WorldCurrencyFormat does not exist', "status": "Error"})

    except WorldCurrencyFormat.DoesNotExist: 
        return Response({"message": 'WorldCurrencyFormat does not exist', "status": "Error"})
        #return JsonResponse({'message': 'The WorldCurrency does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['POST'])
def worldcurrencyformat_test(request):
    try:
        body = request.data
        country = body['country'] if 'country' in body else ""
        currency = body['currency'] if 'currency' in body else ""
        price = body['price'] if 'price' in body else ""

        worldcurrencies = WorldCurrencyFormat.objects.filter(country=country, currency=currency)
        if worldcurrencies:
            worldcurrency = worldcurrencies[0]
            format_currency = returnFormatCurrency(worldcurrency.currency_symbol, worldcurrency.currency_code, worldcurrency.currency_thousand_delimeter, worldcurrency.currency_decimal_delimeter, worldcurrency.currency_symbol_ubication, worldcurrency.display_currency, worldcurrency.bool_cents, None)
            price_format_currency = returnFormatCurrency(worldcurrency.currency_symbol, worldcurrency.currency_code, worldcurrency.currency_thousand_delimeter, worldcurrency.currency_decimal_delimeter, worldcurrency.currency_symbol_ubication, worldcurrency.display_currency, worldcurrency.bool_cents, price)
            dataWCF = {
                "name": worldcurrency.name,
                "country": worldcurrency.country,
                "currency": worldcurrency.currency,
                "currency_symbol": worldcurrency.currency_symbol,
                "currency_code": worldcurrency.currency_code,
                "currency_thousand_delimeter": worldcurrency.currency_thousand_delimeter,
                "currency_decimal_delimeter": worldcurrency.currency_decimal_delimeter,
                "currency_symbol_ubication": worldcurrency.currency_symbol_ubication,
                "bool_cents": worldcurrency.bool_cents,
                "display_currency": worldcurrency.display_currency,
                "format": format_currency,
            }

            return Response({"message": str(price_format_currency), "status": "Success"})
        else:
            return Response({"message": 'WorldCurrencyFormat does not exist', "status": "Error"})

    except WorldCurrencyFormat.DoesNotExist: 
        return Response({"message": 'WorldCurrencyFormat does not exist', "status": "Error"})
        #return JsonResponse({'message': 'The WorldCurrency does not exist'}, status=status.HTTP_404_NOT_FOUND) 
