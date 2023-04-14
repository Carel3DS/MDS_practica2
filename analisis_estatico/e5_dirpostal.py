# Ejercicio 5: dirección postal
# https://regexr.com/7bg09
# Alt: https://regexr.com/7c1dn

import re

texto = input().strip()
patron = r"\b(C\/|Calle) (([A-Z]|[Á-ú])([a-z]|[á-ú])*)\s+(N(º( )?| )?|n(º( )?| )?|)(\d+),?\s+(\d{5})\b"
results = re.findall(patron, texto, flags=re.M)

for match in results:
    cps = match[10]
    nom = match[1]
    dig = match[9]
    print(f"{cps}-{nom}-{dig}")


