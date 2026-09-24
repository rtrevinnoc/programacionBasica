def recibir_entrada(texto):
    entrada = input(texto)
    try:
        return int(entrada)
    except ValueError:
        try:
            return float(entrada)
        except ValueError:
            raise ValueError("La entrada no se puede convertir a un numero")

def recibir_opcion(texto, opciones):
    entrada = input(texto)
    if entrada in opciones:
        return entrada
    else:
        raise KeyError("La opción que ingresó no es valida.")