#EJERCICIOS BASICOS 
"""
#1. Número Par o Impar: Escribe un programa que solicite un número al usuario e imprima si es par o impar. 

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El numero es par")
else: 
    print("El numero es impar")
    

#2. Máximo de Tres Números: Escribe un programa que reciba tres números del usuario y determine cuál es el mayor. 

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print(f"El numero Mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El numero Mayor es: {num2}")
else: 
    print(f"El numero Mayor es: {num3}")

    
#3. Tabla de Multiplicar: Solicita un número al usuario y muestra su tabla de multiplicar hasta el 10 usando un bucle for. 

number = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
"""
    
#4. Suma de Números Naturales: Escribe un programa que sume todos los números naturales desde 1 hasta un número dado por el usuario utilizando un bucle while. 

number = int(input("Ingrese un número: "))


#5. Calculadora Básica: Crea un programa que realice operaciones básicas (+, -, *, /) según la elección del usuario. 
#6. Adivina el Número:Programa un juego donde el usuario deba adivinar un número entre 1 y 100. El programa deberá dar pistas indicando si el número es mayor o menor al número a adivinar. 
#7. Conversor de Temperatura: Crea un programa que convierta de grados Celsius a Fahrenheit y viceversa, dependiendo de la elección del usuario. 
#8. Calculadora de Factorial: Escribe un programa que calcule el factorial de un número ingresado por el usuario utilizando un bucle for o while.