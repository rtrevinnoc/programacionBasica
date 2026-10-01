import csv
from pathlib import Path

def validar_entrada(entrada):
    try:
        return int(entrada)
    except ValueError:
        try:
            return float(entrada)
        except ValueError:
            raise ValueError("La entrada no se puede convertir a un numero")

def recibir_entrada(texto):
    entrada = input(texto)
    return validar_entrada(entrada)

def validar_opcion(entrada, opciones):
    if entrada in opciones:
        return entrada
    else:
        raise KeyError("La opción que ingresó no es valida.")

def recibir_opcion(texto, opciones):
    entrada = input(texto)
    validar_opcion(entrada, opciones)

def recibir_ruta(texto):
    entrada = input(texto)
    ruta = Path(entrada)
    return ruta.resolve()

def procesar_archivo(ruta):
    path = Path(ruta)
    with open(path, mode="r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            yield row