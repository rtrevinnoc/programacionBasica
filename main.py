class Calculadora:
    def __init__(self):
        pass

    def sumar(self):
        pass

    def restar(self):
        pass


def ejecutar_detalles():
    print("--### DETALLES ###--")
    print("Programa de ejemplos del salón 403")
    print("Escrito por Roberto Treviño Cervantes")
 

def ejecutar_salida():
    return


def input_entero(prompt):
    return int(input(prompt))


def operacion_aritmetica():
    pass

opciones = {
    "Salir": ejecutar_salida,
    "Detalles": ejecutar_detalles,
    "Sumar": operacion_aritmetica,
    "Restar": operacion_aritmetica,
}
opciones_lista = list(opciones)
numero_opciones = len(opciones)


def ejecutar_seleccion(opcion):
    seleccion = opciones.get(opcion, None)
    
    if seleccion == None:
        seleccion_numero = int(opcion)

        if seleccion_numero < numero_opciones:
            seleccion = opciones_lista[seleccion_numero]

            funcion_seleccionada = opciones[seleccion]
            funcion_seleccionada()
        else:
            print("#=> No existe la opción")

    else:
        funcion_seleccionada = seleccion
        funcion_seleccionada()


def main():
    print("Iniciando Sistema...")
    print("--### MENU ###--")

    for indice, opcion in enumerate(opciones):
        print(f"{indice}) {opcion}")
 
    opcion = input("Selecciona una opcion: ")
    ejecutar_seleccion(opcion)

 
main()
