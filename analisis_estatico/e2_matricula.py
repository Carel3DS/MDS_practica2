# Ejercicio 2: matrícula
import re

texto = input().strip()
patron2 = "(\W|^)((E(\s|-)?)?\d{4}(\s|-)?[A-Z]{3})(\W|$)"
results = re.findall(patron2, texto)


for match in results:
    print(match[1])

