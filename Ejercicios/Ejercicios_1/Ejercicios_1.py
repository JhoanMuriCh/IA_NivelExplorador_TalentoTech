# Variables y print()
"""
#Declaracion de variables y uso de print()
name= "Juan"
ago= 20
city= "Girardot"
print("Hola, mi nombre es", name, "tengo", ago, "años y vivo en", city)

#suma de enteros
a= 5
b= 10
print("La suma de", a, "y", b, "es", a+b)


#Concatenacion de cadenas
frase1= "Hola, mi nombre es Jhoan, "
frase2= "yo tengo dos hermosos hijos"
print(frase1 + frase2)

#calculo de area de un rectangulo
base= 10
altura= 5
print("El area del rectangulo es", base*altura)

#conversion de unidades
metros= 10
centimetros= metros*100
print(metros, "metros equivalen a", centimetros, "centimetros")

#input() y Operadores Matemáticos

#entrada de datos
name= input("Ingrese su nombre: ")
ago= int(input("Ingrese su edad: "))
print("Hola", name, "tienes", ago, "años")

#suma de enteros
numero1= int(input("Ingrese el primer numero: "))
numero2= int(input("Ingrese el segundo numero: "))
print("La suma de", numero1, "y", numero2, "es", numero1+numero2)

#calculo del perimetro de un cuadrado:
lado= int(input("Ingrese la longitud de un lado del cuadrado: "))
print("El perimetro del cuadrado es", lado*4)

#calculo del promedio
nota1= float(input("Ingrese la primera nota: "))
nota2= float(input("Ingrese la segunda nota: "))
nota3= float(input("Ingrese la tercera nota: "))
print("El promedio de las notas es", (nota1+nota2+nota3)/3)

#calculo de area de un circulo:
radio= int(input("Ingrese el radio del circulo: "))
print("El area del circulo es", 3.1416*radio**2)

#OPERADORES DE ASIGNACIÓN

#asignacion y suma
a= 10
a+= 5
print(a)

#asignacion y resta
b= 50
b-= 20
print(b)

#asignacion y multiplicacion
c= 4
c*= 3
print(c)

#asignacion y division
d= 100
d/= 4
print(d)

#asignacion y modulo
e= 45
e%= 7
print(e)

#OPERADORES DE COMPARACIÓN

#igualdad
a= 5 
b= 4
print(a==b)

#mayor que
c= 10
d= 5
print(c>d)

#menor que
e= 3
f= 7
print(e<f)

#mayor o igual que
g= 10
h= 10
print(g>=h)

#menor o igual que
i= 4
j= 5
print(i<=j)

#OPERADORES LÓGICOS

#conjuncion logica (and)
a= False
b= True
print(a and b)

#disyuncion logica (or)
c= True
d= False
print(c or d)

#negacion logica (not)
e= True
print(not e)


#cambiar operadores logicos
a= True
b= False
c= False
print(b and c, c or a, not a)


#evaluacion de rangos

numero= int(input("Ingrese un numero: "))
#evaluar si el numero esta en el rango de 10 a 20
dentro_del_rango= numero>=10 and numero<=20
#mostrar mensaje segun el resultado de la evaluacion del rango 
mensaje= dentro_del_rango and "el numero esta en el rango" or "el numero no esta fuera del rango"
print(mensaje)


#EJERCICIOS COMBINADOS

#par o impar:

numero= int(input("Ingrese un numero: "))
#evaluar si el numero es par o impar
es_par= numero%2==0
#mostrar mensaje segun el resultado de la evaluacion
mensaje= es_par and "el numero es par" or "el numero es impar"
print(mensaje)

"""
"""
#aprobación de notas:

notaDefinitiva= float(input("ingrese su nota definitiva: "))
#evaluar si la nota es aprobatoria o no
fuera_rango= notaDefinitiva<0 or notaDefinitiva>100

if fuera_rango:
    mensaje= "Nota fuera de rango"
elif notaDefinitiva>=60:
    mensaje= "Aprobado" 
else: 
    mensaje= "Reprobado"

print(mensaje)

"""


#evaluar si la nota esta en el rango de 0 a 100



"""
notaDefinitiva= float(input("ingrese la nota: "))
if notaDefinitiva>=5:
    print("Su nota Excelente")
elif notaDefinitiva>=4:
        print("Su nota Sobresaliente")
elif notaDefinitiva>=3:
        print("Su nota Aceptable")
elif notaDefinitiva>=2:
        print("Su nota Insuficiente")
elif notaDefinitiva<=2 and notaDefinitiva>=0:
    print("Su nota Deficiente")
else:
    print("Nota no aceptada")
"""
"""
#CICLOS FOR EN PYTHON

# Forma 1
ejemplo = [6,4,78,3,6,8,3,2,4,6,7,8,45,4,3,5,6]
texto = "Hola a todos"
for i in ejemplo:
    print(i)

# Forma 2
for i in range(5):
    print ("Hola mundo")

# Forma 3
for i in range(1,11):
    print(i)

# Forma 4
for i in range(20,0,-2):
    print(i)

#programa que muestre la tabla de multiplicar de un numero ingresado por el usuario
numero= int(input("Ingrese un numero: "))

for i in range(1, 11,):
    print(numero, "x", i, "=", numero*i)
    """


#Imprimir los números del 1 al 50: Escribe un programa que imprima todos los números del 1 al 50, uno por línea.
""""
for i in range(1, 51):
    print(i)
"""
#Suma de números impares: Escribe un programa que calcule la suma de todos los números impares entre 1 y 100.
"""
for i in range(1, 101, 2):
    print(i)
"""
#Tabla de multiplicar: Escribe un programa que muestre la tabla de multiplicar del 7, desde el 1 hasta el 10.

for i in range(1, 11):
    print(7, "x", i, "=", 7*i)

#Imprimir los primeros 10 números de Fibonacci: Escribe un programa que imprima los primeros 10 números de la serie de Fibonacci.

fibonacci = [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

for num in fibonacci:
    print(num)

#Determinar si un número es primo: Escribe un programa que determine si un número entero positivo dado por el usuario es un número primo.

numero= int(input("Ingrese un numero: "))
primo= True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break
    

#Factorial de un número: Escribe un programa que calcule el factorial de un número entero positivo dado por el usuario.

numero= int(input("Ingrese un numero: "))
factorial= 1
for i in range(1, numero+1):
    factorial*= i
print("El factorial de", numero, "es", factorial)