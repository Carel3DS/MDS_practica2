# Ejercicio 4: correo
import re

texto = input().strip()
patron = r"\b([a-z]+?)\.([a-z]*?)(\.(\d{4}))?\@((alumnos\.)?urjc\.es)\b"
results = re.findall(patron, texto, flags=re.M)

for match in results:
    if match[4] == "alumnos.urjc.es":
        print(f"alumno {match[1]} matriculado en {match[3]}")
    else:
        print(f"profesor {match[0]} apellido {match[1]}")


