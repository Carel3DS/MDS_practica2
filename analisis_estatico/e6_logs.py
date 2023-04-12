# Ejercicio 6: logs
# https://regexr.com/7bg63

import re

texto = input().strip()
patron = r"(INFO) .*--- \[(.+)\].*?(\w+) : (.*)"
results = re.findall(patron, texto, flags=re.M)

# Nota: devolverías el match entero, pero hay que imprimirlo de una forma específica
for match in results:
    for group in match:
        if group == match[-1]:
            print(f'"{group}"')
        else:
            print(f'"{group}",', end="")


