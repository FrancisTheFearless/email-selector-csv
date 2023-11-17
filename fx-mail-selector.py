import csv
import re

# Ruta del archivo CSV de entrada
archivo_entrada = 'bbdd.csv'

# Ruta del archivo CSV de salida
archivo_salida = 'lista-limpia.csv'

# Conjunto para almacenar los correos electrónicos únicos
correos_unicos = set()

# Expresión regular para identificar correos electrónicos
regex_correo = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Leer el archivo CSV
with open(archivo_entrada, mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo, delimiter=';')
    for fila in lector:
        for campo in fila:
            correos_encontrados = regex_correo.findall(campo)
            for correo in correos_encontrados:
                correos_unicos.add(correo)

# Escribir los correos en un nuevo archivo CSV
with open(archivo_salida, mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    for correo in correos_unicos:
        escritor.writerow([correo])

print(f"Total de correos electrónicos únicos recogidos: {len(correos_unicos)}")
print(f"Correos extraídos con éxito en {archivo_salida}")
