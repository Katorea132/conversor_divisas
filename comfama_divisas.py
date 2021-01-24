#!/usr/bin/python3
"""
Este modulo se encarga de inicializar el script y hacer la conversion
de la moneda inicial a la deseada
"""

import json
import requests
from input_validators import check_arguments


url_api = "https://api.binance.com/api/v3/ticker/price?"


def main(starting=None, old=None, final=None):
    starting_currency, old_amount, final_currency = check_arguments(
        starting, old, final)
    compound_currency = starting_currency + final_currency
    compound_currency_reversed = final_currency + starting_currency
    new_amount = 0.0
    currencies = requests.get(url_api).json()
    for currency in currencies:
        if currency['symbol'] == compound_currency:
            new_amount = float(currency['price']) * old_amount
            break
        elif currency['symbol'] == compound_currency_reversed:
            new_amount = old_amount / float(currency['price'])
            break

    return json.dumps({
        'starting_currency': starting_currency,
        'old_amount': old_amount,
        'final_currency': final_currency,
        'new_amount': new_amount
        })


if __name__ == "__main__":
    print(main())
