opciones = [
    "Salir",
    "Detalles",
    "Sumar"
]

def ejecutar_detalles():
    print("--### DETALLES ###---")
    print("Programa de ejemplo del salón 403")
    print("Escrito por Roberto Treviño Cervantes")

def ejecutar_salida():
    return

def ejecutar_suma():
    return 2 + 2

def seleccionar_opcion(opcion):
    if opcion == 0:
        ejecutar_salida()
    elif opcion == 2:
        print(ejecutar_suma())
    else:
        ejecutar_detalles()

def main():
    print("Iniciando Sistema...")
    print("--### MENU ###--")
    print("0) " + opciones[0])
    print("1) " + opciones[1])
    print("2) " + opciones[2])

    entrada = int(input("Selecciona una opción: "))
    seleccionar_opcion(entrada)

main()