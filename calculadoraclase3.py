# # Actividad 1: Mejorando la calculadora

# # Refactorizar el script de la calculadora lineal en al menos 4 funciones separadas. una por cada tipo de operación. Como ser: Sumar(), Restar(), Multiplicar() y Dividir()

# # Añadir manejo de excepciones para entradas inválidas y división por cero.

# Actividad 2: Git y Github

# Git local

# Crear una carpeta nueva para el proyecto de calculadora.

# Inicializar un repositorio con git init.

# Agregar y confirmar cambios con git add y git commit.

# GitHub

# Crear una cuenta en github.com si no tenés una.

# Crear un nuevo repositorio desde tu perfil (usá el mismo nombre del proyecto).

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("no se puede dividir por cero")
    return a / b


def calculadora():
    print("Bienvenido a la calculadora")
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Seleccione la operación que desea realizar: 1) Sumar 2) Restar 3) Multiplicar 4) Dividir")
        opcion = int(input("Ingrese el número de la operación del 1 al 4: "))

        if opcion == 1:
            resultado = sumar(a, b)
        
        elif opcion == 2:
            resultado = restar(a, b)
            
        elif opcion == 3:
            resultado = multiplicar(a, b)
            
        elif opcion == 4:
            resultado = dividir(a, b)
            
        else:
            print("Opción inválida, por favor ingrese un número del 1 al 4")
            return
        print(f"El resultado es :  {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Gracias por usar la calculadora")


if __name__ == "__main__": 
    calculadora()



