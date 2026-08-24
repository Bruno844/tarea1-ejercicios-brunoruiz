#Ejercicio 1 Datos personales
#Crear un programa que almacene en variables:

# Nombre
#Edad
#Ciudad
#Altura

#Luego mostrar todos los datos por pantalla. Ademas, utilizar type() para mostrar el tipo de cada variable.

nombre = "bruno"

edad = "34"

ciudad = "toronto"

altura = 1.60


print(type(nombre))
print(type(edad))
print(type(ciudad))
print(type(altura))

###-------------------------------------------------------------------------------------------------------------



'''

Ejercicio 2 — Conversión de tipos
Solicitar al usuario mediante input():
• Nombre
• Edad
• Altura

La edad debe convertirse a int y la altura a float. Mostrar los datos ingresados y sus respectivos tipos.

'''

nombre = input("ingrese su nombre")
edad = int(input("ingrese su edad"))
altura = int(input("ingrese su altura"))

print(f"nombre: {nombre}, edad: {edad}, altura: {altura}")


###-----------------------------------------------------------------------------------------------------------



'''

Ejercicio 3 — Operaciones matemáticas
Solicitar dos números al usuario y mostrar:
• Suma
• Resta
• Multiplicación
• División
• Resto de la división

Ejemplo: si los números son 10 y 3, mostrar Suma: 13, Resta: 7, Multiplicación: 30, División: 3.333... y Resto: 1.



'''


num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))

suma = num1 + num2

resta = num1 - num2

multi = num1 * num2

div = num1 / num2

resto = num1 % num2

print(f"suma: {suma}, resta: {resta}, multi: {multi}, div: {div}, resto: {resto}")


###------------------------------------------------------------------------------------------------------------------


'''

Ejercicio 4 — Mayor de edad
Solicitar al usuario su edad. Utilizar una estructura if para determinar si es mayor de edad o menor de edad.


'''


edad = int(input("ingrese su edad"))

if (edad >= 18):
    print("es mayor")
else:
    print("no es mayor")


###-----------------------------------------------------------------------------------------------------------------


#ejercicio 5



numero = float(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")




###---------------------------------------------------------


#ejercicio 6


numeros = [10, 25, 8, 40, 15, 30]

# 1. La lista completa
print("Lista completa:", numeros)

# 2. El primer elemento
print("Primer elemento:", numeros[0])

# 3. El último elemento
print("Último elemento:", numeros[-1])

# 4. La cantidad de elementos utilizando len()
print("Cantidad de elementos:", len(numeros))




###-----------------------------------------------------------


#ejercicio 7

nombres = ["Ana", "Pedro", "Laura", "Juan", "Sofía"]

for nombre in nombres:
    print(nombre)





# ----------------------------------------------------------



#ejercicio 8

notas = [8, 4, 6, 10, 3, 7, 5]

for nota in notas:
    if nota >= 6:
        print(f"Nota {nota}: Aprobado")
    else:
        print(f"Nota {nota}: Desaprobado")




#-------------------------------------------------------------




#ejercicio 9


numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    print(i)



#--------------------------------------------------------------


#ejercicio 10


alumnos = ["Ana", "Pedro", "Laura", "Juan"]
notas = [8, 5, 9, 4]

for alumno, nota in zip(alumnos, notas):
    estado = "Aprobado" if nota >= 6 else "Desaprobado"
    print(f"{alumno} - {nota} - {estado}")
