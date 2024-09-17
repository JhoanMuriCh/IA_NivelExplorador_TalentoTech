#EJERCICIO MANEJO DE IF
#Realizar un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú
#1- Establecer el menu de opciones
print('Menú')
print('1- Sumar')
print('2- Restar')
print('3- Multiplicar')
#2- Leer la opción
opcion = int(input('Digite el número de la operación a realizar: '))
#3- Leer los números por teclado
num1 = float(input('Digite el primer número '))
num2 = float(input('Digite el segundo número'))
#4- Realizar la operación correspondiente
if opcion == 1:
    print(f'El resultado es: {num1+num2}')
elif opcion == 2:
    print(f'El resultado es: {num1-num2}')
elif opcion == 3:
    print(f'El resultado es: {num1*num2}')
else:
    print('Opción no valida.')


