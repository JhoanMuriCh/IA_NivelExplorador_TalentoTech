#FUNCIONES EN PYTHON
#Funcion pow() devuelve la potencia de un número
a=5
b=3
print(a**b)
print(pow(a,b))

#Funcion split sirve para separar una cadena de texto en una lista o interable
a=int(input('Digite un número'))
b=int(input('Digite un número'))
c=int(input('Digite un número'))
a,b,c = input('Digite tres números separados por coma: ').split(",")
print(a)
print(b)
print(c)

#funcion len() devuelve la longitud de un objeto iterable
texto = "Python"
ejemplo = [2,5,'t',9.2,True]
print(len("Hola a todos"))

#funcion sin parametros (no ejecuta nada) 
def saludar():
    print('Hola, bienvenidos a talento tech.')
    saludar() #para que ejecute la funcion hay que llamarla

#funcion con parametros 
def sumar(a,b):
    return a + b
print(sumar(5,3)) #para que ejecute hay que darle los parametros

def area_circulo(radio):
    pi=3.1416
    area=pi*pow(radio,2)
    return area
    # otra opcion es: return 3.1416 * radio ** 2

perro =input('Digite el radio del circulo: ')
print(f'El área del circulo es: {area_circulo(perro)}')

#Definimos las funciones
#Función sumar
def sumar(a,b):
    return a+b
#Función restar
def restar(a,b):
    return a-b
#Función multiplicar
def multiplicar(a,b):
    return a*b
#Función división
def dividir(a,b):
    if b!=0:
        return a/b
    else:
        return 'Error, la división por cero no existe.'
#Función menu
def menu():
    print('Bienvenidos a mi calculadora')
    #Menu de opciones
    print('Seleccione una operación: ')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Salir')
#Función salir 
def salir():
    op = input('Digite s para continuar o n para salir: ')
    if op=='s':
        menu()
    else:
        exit()
def calculadora():
    opcion=0
    while opcion !=5:
        menu()
        opcion = int(input('Digite el número de la operación a realizar: '))
        if opcion == 1:
            num1 = float(input('Digite el primer número'))
            num2 = float(input('Digite el segundo número'))
            print(f'La suma es: {sumar(num1,num2)}')
            salir()
        elif opcion == 2:
            num1 = float(input('Digite el primer número'))
            num2 = float(input('Digite el segundo número'))
            print(f'La resta es: {restar(num1,num2)}')
            salir()
        elif opcion == 3:
            num1 = float(input('Digite el primer número'))
            num2 = float(input('Digite el segundo número'))
            print(f'La multiplicación es: {multiplicar(num1,num2)}')
            salir()
        elif opcion == 4:
            num1 = float(input('Digite el primer número'))
            num2 = float(input('Digite el segundo número'))
            print(f'La división es: {dividir(num1,num2)}')
            salir()
        else:
            print('Opción no valida.')
calculadora()


