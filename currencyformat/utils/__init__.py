import re

def returnFormatCurrency(currency_symbol, currency_code, currency_thousand_delimeter, currency_decimal_delimeter, currency_symbol_ubication, display_currency, bool_cents, price=None):
    '''
    ● Currency can display currency code or symbol
    ● Currency can be shown after or before price
    ● Show cents or no cents
    ● Display formats such as #,###.## or #.###,##
    '''
    format_currency = ""

    value_display = ""
    if display_currency == "code":
        value_display = currency_code
    if display_currency == "symbol":
        value_display = currency_symbol

    price_miles = ""
    price_cents = ""
    if price is not None:
        if "." in price or "," in price:
            if "." in price:
                price_split1 = price.split(".")
                if len(price_split1) > 1:
                    last_position_price = price_split1[len(price_split1)-1]
                    if len(last_position_price) == 2:
                        #Tiene decimales
                        price_cents = price_split1[len(price_split1)-1]
                        price_miles = price_split1[0]
            if "," in price:
                price_split2 = price.split(",")
                if len(price_split2) > 1:
                    last_position_price = price_split2[len(price_split2)-1]
                    if len(last_position_price) == 2:
                        #Tiene decimales
                        price_cents = price_split2[len(price_split2)-1]
                        price_miles = price_split2[0]
        price_miles = price_miles.replace(",", "").replace(".", "")
                        
    value_cents = ""
    if bool_cents:
        if price is None:
            value_cents = currency_decimal_delimeter + "##"
        else:
            value_cents = currency_decimal_delimeter + str(price_cents)

    value_miles = ""
    if price is None:
        value_miles = "#" + currency_thousand_delimeter + "###"
    else:
        string_commas = "{:,}"
        number_with_commas = string_commas.format(int(price_miles))

        if currency_thousand_delimeter == ",":
            value_miles = number_with_commas
        if currency_thousand_delimeter == ".":
            number_with_dots = number_with_commas.replace(",", ".")
            value_miles = number_with_dots

    if currency_symbol_ubication == "left":
        format_currency = value_display + value_miles + value_cents
    elif currency_symbol_ubication == "right":
        format_currency =  value_miles + value_cents + value_display
    else:
        format_currency =  value_miles + value_cents

    return format_currency