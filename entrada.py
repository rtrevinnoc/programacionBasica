def recibir_entrada(texto):
    entrada = input(texto)
    if entrada.isdigit():
        return int(entrada)
    elif "." in entrada:
        return float(entrada)
    else:
        return False

def recibir_opcion(texto, opciones):
    entrada = input(texto)
    if entrada in opciones:
        return entrada
    else:
        return False