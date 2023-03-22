# Ejercicio 1: Años
# PRUEBA: 2002  1991  9999  0000  2001. 2001,.2001,,2001, 12345678901234567890
import re

texto = input().strip()
patron2 = "(\D|^)(\d{4})(\D|$)"
results = re.findall(patron2, texto,flags=re.M)


for match in results:
    print(match[1])

