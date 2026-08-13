def ejecutar_detalles():
    print("--### DETALLES ###--")
    print("Programa de ejemplos del salón 403")
    print("Escrito por Roberto Treviño Cervantes")
 

def ejecutar_salida():
    return
 

def ejecutar_suma():
    print(2 + 2)


def ejecutar_resta():
    print(4 - 2)


opciones = {
    "Salir": ejecutar_salida,
    "Detalles": ejecutar_detalles,
    "Sumar": ejecutar_suma,
    "Restar": ejecutar_resta,
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
