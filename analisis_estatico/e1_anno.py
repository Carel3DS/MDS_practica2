# Ejercicio 1: Años
# PRUEBA: 2002  1991  9999  0000  2001. 2001,.2001,,2001, 12345678901234567890
import re

texto = input().strip()
patron1 = "^(\d{4})[\s]"
patron2 = "[\s\.\,](\d{4})[\s\.\,]"
results = re.findall(patron1, texto)
results += re.findall(patron2, texto)


for match in results:
    print(match)

