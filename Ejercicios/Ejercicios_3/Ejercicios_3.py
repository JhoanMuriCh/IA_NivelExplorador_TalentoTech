#Ejercicios Básicos
"""
#Escribe un programa que cree una lista con los números del 1 al 10 e imprima cada número en una línea separada.
numeros = [1,2,3,4,5,6,7,8,9,10]
for i in numeros:
    print(i)

#Dada la lista ['manzana', 'naranja', 'plátano', 'uva'], imprime el primer y último elemento de la lista.
frutas = ['manzana', 'naranja', 'plátano', 'uva']
print(frutas[0])
print(frutas[3])

#Escribe un programa que agregue el número 11 a una lista de números del 1 al 10.
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.append(11)

#Dada la lista ['perro', 'gato', 'conejo', 'pájaro'], elimina el tercer elemento e imprime la lista actualizada.
animales = ['perro', 'gatos', 'conejo', 'pájaro']
animales.pop(2)
print(animales)

#Crea una tupla con los días de la semana e imprime el tercer día.
dia_semana = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')
print(dia_semana[2])

#Escribe un programa que convierta la lista ['rojo', 'verde', 'azul'] en una tupla.
colores = ['rojo', 'verde', 'azul']
colores = tuple(colores)

#Crea un diccionario con los nombres de 3 estudiantes y sus edades. Luego imprime la edad de un estudiante dado su nombre.
estudiantes = {
    'Juan': 25, 
    'Pedro': 30, 
    'Luis': 28
    }
print(estudiantes['Juan'])

#Dado el diccionario { 'A': 1, 'B': 2, 'C': 3 }, agrega un nuevo par clave-valor ('D', 4) y elimina la clave 'B'
diccionario = { 'A': 1, 'B': 2, 'C': 3 }
diccionario['D'] = 4
diccionario.pop('B')

#Dada la lista ['a', 'b', 'c', 'd'], imprime cada elemento de la lista utilizando un ciclo for.
lista = ['a', 'b', 'c', 'd']
for i in lista:
    print(i)

#Dado el diccionario { 'nombre': 'Ana', 'edad': 20, 'ciudad': 'Bogotá' }, imprime todos los valores del diccionario.
diccionario = { 
    'nombre': 'Ana',
    'edad': 20,
    'ciudad': 'Bogotá'
    }
print(diccionario.items())
"""
"""
#EJERCIOCIOS INTERMEDIOS

#Sumar elementos de una lista:
#Escribe un programa que sume todos los números de una lista.
numeros = [1,2,3,4,5,6,7,8,9,10]
suma = 0
for i in numeros: #i es el valor de la lista
    suma += i
print(suma)
"""
#Listas y números pares:
#Crea una lista de números del 1 al 20. Filtra y crea una nueva lista que contenga solo los números pares.
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(2,21,2):
    print(i)

#Buscar elementos en una lista:
#Dada una lista de nombres, permite que el usuario ingrese un nombre y determina si ese nombre está en la lista.
nombres = ['juan', 'andres', 'maria', 'pedro']
nombres.append(str('Ingrese nombre: '))
deteminar_nombre = input('Ingrese nombre para observar si se encuentra en la lista: ')
if nombres == deteminar_nombre:
    print(True)
else:
    print(False)



