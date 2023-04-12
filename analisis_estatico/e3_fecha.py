# Ejercicio 3: fecha
import re

texto = input().strip()
patron2 = r"\b(\d{4})\-(\d{2})\-(\d{2})\b"
results = re.findall(patron2, texto, flags=re.M)

print(re.sub(patron2, r"\3.\2.\1", texto))
