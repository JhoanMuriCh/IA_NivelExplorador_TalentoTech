#EJERCICIO MANEJO DE WHILE
#Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo
lista = [0,1,2,3,4,5,6,7,8,9]
num = -1  # Inicializamos la variable num con un valor que no se encuentra en la lista
while num<0 or num>9:
    num = int(input('Digite un número del 0 al 9: '))
    if num in lista:
        print('El número se encuentra en la lista')
        break
    else:
        print('El número no se encuentra en la lista')
        break
