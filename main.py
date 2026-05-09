#variables y asignacion

#aqui puedo ingresar etras y numero y no rompe. 
# edad = input("ingrese su edad ")

# edad = int(input("ingrese edad"))
#si ingreso letras rompe, por lo que es mas especifico
#print(edad)
#print(type(edad)) #me da como resultado el tipo de esa variable

# 0 => 10 (me imprime el rango del numero que yo le ortorge)
#print(*range(11))
#print(*range(5,11))#imprime del 5 al 11

#print(*range(0,21,2))# el tercer numero es el salto que quiero dar en el recorrido del 0 al 21

#Condicionales(una estructura de control)

#nota = int(input("ingrese una nota : "))

#if condicion: (siempre tengo que agregar la condicion variable y los dos puntos y tabular)
    #print("")
#para que no se superpongan las condiciones se usan
#los operadores logico

#x = 5
#evalua si las dos son erdaderas para que sea true
#print( x > 3 and x <= 10 )
#evalua si uno de los dos es verdadero. si o si tiene que cumplirse uno de ellos
#print(x > 3 or x <= 10 )

#if nota < 0 or nota >10:
#    print("ingresa una nota valida del 0 al 10")
#else: 
#   if nota >= 9:
#       print("exelente")
#   elif nota >= 6:
#       print("aprobado")
#   else:
#      print("desaprobado")
#     
#    #Estructuras de control repetitivo
#bajo un ciclo de repticion que es lo que debe de hacer
# #de acuerdo a cierta repeticion

# for i in range(11):
#     nota = input("ingrese nota: ")
#     if nota == "salir":
#         break
    
#     nota_final = int(nota)
    
#     if nota_final > 0 and nota_final <= 10:
#         if nota_final >= 9:
#             print("exelente")
#         elif nota_final >= 6:
#             print("aprobado")
#         else:
#             print("desaprobado")
#     else:
#         print("ingresa una nota valida del 1 - 10.")

#necesito de una variable iteradora. y le damos el valor de cuanto queremos que se repita el ciclo.

i = 0
while i < 5 :
    i = i + 1
    print(i)
    
    saludo = "hola mundo!"
    for i in saludo:
        print(i)
        #el for saabe cuando termina por que itera cada letra de saludo y termina cuando termina de contar.
        #el while necesita de una variable iteradora para saber cuando termina, si no se le asigna un valor a esa variable iteradora el ciclo se vuelve infinito.
        # el for es mas especifico que el while, el for sabe cuando termina, el while no sabe cuando termina.