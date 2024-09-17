#LISTAS, TUPLAS, DICCIONARIOS

#listas vacia
datos = [] 

#lista con elementos
datos1= [18, 20, 37, 24, 19, 17, 21] #lista con elementos de tipo entero
datos2= [1.72, 1.65, 1.80, 1.55, 1.89, 1.90] #lista con elementos de tipo flotante
datos3= ['Juan', 'Ana', 'Pedro', 'Juan','Carolina'] #lista con elementos de tipo cadena
datos4= [18, 1.65, True, 'Hola'] #lista con elementos de diferentes tipos

#operaciones con listas
#acceder a un elemento de la lista
print(datos1[2]) #imprime el tercer elemento de la lista datos1
#modificar un elemento de la lista
print(datos1)
datos1[1]= 366 #tambien podemos poner un imput para que el usuario digite el valor
print(datos1)

#gregar un elemento a la lista (append: agrega un elemento al final de la lista)
print(datos2)
datos2.append(float(input('Digite un número: '))) #agrega el valor 23 al final de la lista
print(datos2)

#agregar un elemento en una posición específica (insert: agrega un elemento en la posición que se le indique)
print(datos3)
datos3.insert(int(input('Digite la posición: ')), input('Digite el nombre: ')) #agrega el nombre en la posición que se le indique

#eliminar un elemento de la lista (remove: elimina el primer elemento que coincida con el valor que se le indique)
print(datos1)
datos1.remove(366) #elimina el valor 366 de la lista
print(datos1)

#eliminar un elemento de la lista por posición (pop: elimina el elemento de la posición que se le indique)
print(datos2)
datos2.pop(2) #elimina el tercer elemento de la lista
print(datos2)

#eliminar un elemento de la lista por posición (del: elimina el elemento de la posición que se le indique)
print(datos3)
del datos3[2] #elimina el tercer elemento de la lista
print(datos3)


#contatenar listas (extend: agrega los elementos de una lista a otra)
print(datos1)
print(datos2)
datos1.extend(datos2) #agrega los elementos de la lista datos2 a la lista datos1
print(datos1)

print(datos1+datos2) #concatena las dos listas
print(datos1*2) #repite la lista dos veces
print(len(datos1)) #imprime la longitud de la lista
print(datos1.count(18)) #cuenta cuantas veces se repite el valor 18 en la lista
print(datos1.index(18)) #imprime la posición del valor 18 en la lista
print(datos1.index(18, 1)) #imprime la posición del valor 18 en la lista a partir de la posición 1

#Ejercicio: crea una lista con las frutas o comida favoritas de ustedes, y aplicar las funciones vistas.
print("Las frutas favoritas de Juan son: ")
frutas = ['manzana', 'pera', 'uva', 'fresa', 'mango']
print(frutas)
print(len(frutas))
print("Pero mis Frutas favoritas son: ")
frutas.insert(1, 'arandanos')
frutas.pop(5)
frutas.insert(2, "mango")
frutas.append("kiwi")
print(frutas)
print(len(frutas))


