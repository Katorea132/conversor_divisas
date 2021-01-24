# Conversor de Divisas
Este proyecto es un script de python que convierte alguna de las divisas
permitidas (BTC, BCC, LTC, ETH, ETC, XRP) a alguna otra de la misma
lista (diferente a la inicial).
Retorna un string con formato de JSON que contiene el nombre de la moneda
inicial, la cantidad de esa moneda, el nombre de la moneda a la que se desea
convertir y el valor equivalente en esta última.

Se puede llamar a main como una función desde otro script, pasándole los 3
argumentos necesario en forma de string: Nombre de la moneda, cantidad, y
moneda objetivo. También se puede llamar como script directamente, similar
a "python3 main.py BTC 123 BCC" o tiene modo interactivo, es decir,
el script pedirá cualquier dato faltante mediante ingreso manual.
