from aritmetica import operaciones, division, multiplicacion, resta, suma
from es.entrada import recibir_opcion, recibir_entrada

if __name__ == "__main__":
    print(f"{"*" * 6} MENU {"*" * 6}")

    while True:
        try:
            opcion = recibir_opcion("Introduce una opción: ", operaciones)
        except KeyError as error:
            print("La opción que ingresó no es valida. Las opciones disponibles son: {', '.join(operaciones.keys())}.")
            opcion = recibir_opcion("Introduce nuevamente una opción: ", operaciones)

        try:
            a = recibir_entrada("Introduce un numero: ")
        except ValueError:
            a = recibir_entrada("Vuelve a introducir un numero: ")

        try:
            b = recibir_entrada("Introduce otro numero: ")
        except ValueError:
            b = recibir_entrada("Vuelve a introducir otro numero: ")

        try:
            resultado = operaciones[opcion](a, b)
        except KeyError:
            print(f"La opción que ingresó no es valida. Las opciones disponibles son: {', '.join(operaciones.keys())}.")
        except ZeroDivisionError:
            print("No se puede ejecutar la operación de división con un denominador 0.")
        except (TypeError, NameError):
            print("Ocurrió un error fatal. Vuelve a intentarlo.")
        else:
            print(f"#=> {resultado}")
        finally:
            print("El programa continua")