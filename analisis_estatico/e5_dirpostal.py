# Ejercicio 5: dirección postal
# https://regexr.com/7bg09

import re

texto = input().strip()
patron = r"\b(C\/|Calle) ([A-Za-z]*) (N(\º( )?| )?|n(\º( )?| )?|)(\d+),? (\d{5})\b"
results = re.findall(patron, texto, flags=re.M)

for match in results:
    cps = match[8]
    nom = match[1]
    dig = match[7]
    print(f"{cps}-{nom}-{dig}")


