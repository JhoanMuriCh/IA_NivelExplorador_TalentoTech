#EJERCICIO MANEJO DE FOR
#Realiza un programa que pida al usuario cuantos números quiere introducir.
#Luego lee todos los números que se han introducido y se realiza una operación de media aritmética

#pedir al usuario cuantos números quiere introducir
cantidad = int(input('¿Cuantos numeros quieres introducir? '))
#iniciar una lista vacia, para guardar los números
numeros = []
#capturar los números y agregarlos a la lista
for _ in range(cantidad):
    numero = float(input(f'Digite el número: '))
    numeros.append(numero)
#calcular la media aritmética
media = sum(numeros)/cantidad

print(f'La media aritmética es: {media}')
