#DUPLAS

#Una dupla es una colección de elementos ordenados que no se pueden modificar. Se definen con paréntesis y los elementos se separan por comas.
#Ejemplo:
dupla = (1,2,3,4,5)
print(dupla)
#Para acceder a un elemento de la dupla se hace igual que con las listas, indicando la posición del elemento que se quiere acceder.
print(dupla[2])
#Para modificar un elemento de la dupla se debe convertir la dupla en lista, modificar el elemento y volver a convertir la lista en dupla.
#Ejemplo:
print(dupla)
lista = list(dupla)
lista[1] = 6
dupla = tuple(lista)
print(dupla)
#Para eliminar una dupla se usa la palabra reservada del.
#Ejemplo:
del dupla
#Para concatenar duplas se usa el operador +.
#Ejemplo:
dupla1 = (1,2,3)
dupla2 = (4,5,6)
dupla3 = dupla1 + dupla2