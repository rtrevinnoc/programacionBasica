from division import division
from multiplicacion import multiplicacion
from resta import resta
from suma import suma
from entrada import recibir_opcion, recibir_entrada

if __name__ == "__main__":
    print(f"{"*" * 6} MENU {"*" * 6}")

    opciones = {
        "suma": suma,
        "resta": resta,
        "divison": division,
        "multiplicacion": multiplicacion
    }

    opcion = recibir_opcion("Introduce una opción: ", opciones)

    a = recibir_entrada("Introduce un numero: ")
    b = recibir_entrada("Introduce otro numero: ")

    resultado = opciones[opcion](a, b)

    print(f"#=> {resultado}")