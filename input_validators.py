#!/usr/bin/python3
"""
Este modulo contiene las funciones encargadas de la validacion
de los input, tambien se encarga de determinar el metodo de entrada
para su ejecucion
"""
import re
import sys

allowed_currencies = {"BTC", "BCC", "LTC", "ETH", "ETC", "XRP"}


def check_currency(currency):
    """Determina si el parametro pasado como moneda es valido o no

    Args:
        currency (str): la moneda, en forma de string

    Raises:
        ValueError: Se levante el error si el valor no es una de las
        monedas validas

    Returns:
        str: Retorna la moneda de ser valida
    """
    if currency not in allowed_currencies:
        raise ValueError("La moneda " + currency + " no es permitida")
    return currency


def check_amount(amount):
    """Verifica que el parametro de la cantidad de dinero sea valido.
    Es decir, que empiece por un numero del 1 al 9, este separado
    por un punto de sus valores decimales y que solo contenga
    numeros dentro de si

    Args:
        amount (str): la cantidad en forma de string

    Raises:
        TypeError: Se eleva si el numero no cumple con las condiciones
        para ser considerado como un valor monetario valido

    Returns:
        float: el numero en forma de float si es valido
    """
    try:
        if re.match(r'^[0-9]\d*(\.\d{1,2})?', amount):
            return float(amount)
        else:
            raise TypeError()
    except Exception:
        raise TypeError("Por favor, verifique que la cantidad tenga un \
formato correcto")


def check_arguments(starting, old, final):
    """Se encarga de determinar el metodo por el cual los argumentos
    estan siendo proporcionados, ademas, valida que cada uno de los
    argumentos tenga valores correctos mediante las funciones auxiliares
    check_amount y check_currency

    Args:
        starting (str): Argumento utilizado si se llama main como funcion
        old (str): Argumento utilizado si se llama main como funcion
        final (str): Argumento utilizado si se llama main como funcion
    """
    if starting and old and final:
        starting_currency = check_currency(starting)
        amount_starting_currency = check_amount(old)
        final_currency = check_currency(final)
    elif len(sys.argv) == 4:
        starting_currency = check_currency(sys.argv[1])
        amount_starting_currency = check_amount(sys.argv[2])
        final_currency = check_currency(sys.argv[3])
    elif len(sys.argv) == 3:
        starting_currency = check_currency(sys.argv[1])
        amount_starting_currency = check_amount(sys.argv[2])
        final_currency = check_currency(input("Por favor, ingrese la \
moneda de salida: "))
    elif len(sys.argv) == 2:
        starting_currency = check_currency(sys.argv[1])
        amount_starting_currency = check_amount(input("Por favor, ingrese \
la cantidad: "))
        final_currency = check_currency(input("Por favor, ingrese la \
moneda de salida: "))
    elif len(sys.argv) == 1:
        starting_currency = check_currency(input("Por favor, ingrese la \
moneda de entrada: "))
        amount_starting_currency = check_amount(input("Por favor, ingrese \
la cantidad: "))
        final_currency = check_currency(input("Por favor, ingrese la \
moneda de salida: "))
    else:
        raise KeyError("Cantidad excesiva de argumentos!")

    if final_currency == starting_currency:
        raise ValueError("Por favor, verifique que las monedas sean distintas")
    return starting_currency, amount_starting_currency, final_currency
