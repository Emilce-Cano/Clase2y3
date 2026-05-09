# Actividad 1:

# Define variables para almacenar el nombre, edad y profesión del usuario.

# Solicita estos datos por teclado utilizando input().

# Imprime en pantalla un mensaje personalizado incluyendo todos estos datos.

# Actividad 2:

# Escribe un pequeño script que utilice un bucle para mostrar los primeros 10 números pares.

# Usa condicionales para validar y mostrar sólo los números pares.

#1)
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))
# profesionDeUsuario = input("Ingrese su profesion de usuario: ")

# print(f"hola {nombre}, su edad es de {edad}, y su profesion de usuario es {profesionDeUsuario}.")

#2)
# for i in range(2,21,2):
#     #print(i) mostrara solo los numero pares
    
    
#     if i % 2 == 0:#si el numero es divisible por 2, entonces es un numero par valida si es par y mostrara solo los paresimprimiendo
#         print(f"{i} es un numero par.")
        
# #CALCULADORA BASICA IMPLEMENTANDO LO VISTO con un enfoque lineal. 

# num1 = float(input("Ingrese el primer numero: "))
# num2 = float(input("ingrese el segundo numero: "))
# operacion = input("Ingrese la operacion a realizar (+, -, *, /): ")

# if operacion == "+":
#     resultado = num1 + num2
#     print(f"el resultado es: {resultado}")
# elif operacion == "-":
#     resultado = num1 - num2
#     print(f"el resultado es: {resultado}")
# elif operacion == "*":
#     resultado = num1 * num2
#     print(f"el resultado es: {resultado}")
# elif operacion == "/":
#     resultado = num1 / num2
#     print(f"el resultado es: {resultado}")
# else:
#     print("operacion no valida, por favor ingrese una operacion correcta.")
    
    #calculadora de la clase. 
    
while True:
        print("\n =========Bienvenido a la calculadora========")
        print("\n Opciones: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        
        opcion= int(input("elija la opcion del 1 - 4): "))
    
        if opcion not in [1,2,3,4]:
            print("opcion no valida, por favor ingrese una opcion del 1 al 4.")
            continue
        
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        
        
        # if opcion == 1:
        #     result = a+b
        # elif opcion == 2:
        #     result = a-b
        # elif opcion == 3:
        #     result = a*b
        # elif opcion == 4:
        #     if b== 0:
        #         print("no se puede dividir por 0")
        #     else:
        #         result = a/b
        match opcion:
            case 1:
                result = a+b
                print(f"el resultado es: {result}")
            case 2:
                result = a-b
                print(f"el resultado es: {result}")
            case 3:
                result = a*b
                print(f"el resultado es: {result}")
            case 4:
                if b == 0:
                    print("no se puede dividir por 0")
                else:
                    result = a/b
                    print(f"el resultado es: {result}")
        
            
        otra = input("desea realizar otra operacion s/n ?")
        if otra != "s":
            print("hasta la proxima")
            break
        