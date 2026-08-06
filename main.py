def seleccionar_opcion(opcion):
    print(opcion)

def main():
    print("Iniciando Sistema...")
    print("--### MENU ###--")
    print("0) Salir")
    print("1) Detalles")

    entrada = input("Selecciona una opción: ")
    seleccionar_opcion(entrada)

main()