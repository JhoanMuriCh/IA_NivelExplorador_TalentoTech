#DICCIONARIOS

#clave.valor {}

#diccionario vacio
datos = {}

#diccionario con elementos
estudiantes= {
    'nombre': 'Andres',
    'apellido': 'Gomez',
    'edad': 18,
    'cuidad': 'Medellin',
}
print(estudiantes)
#acceder a un elemento del diccionario
print(estudiantes['nombre'])

#modificar un valor
estudiantes['edad']= int(input('Digite su edad: '))
print (estudiantes)

#agregar nuevo par clave:valor
estudiantes['profesión']= input('Digite su profesión: ')
print(estudiantes)

#eliminar un par clave:valor
estudiantes.pop('cuidad') #(input('Digite la clave a eliminar: ')) también se puede solicitando al usuario.
print(estudiantes)

#Imprimir las claves o keys
print(estudiantes.keys())

#imprimir los valores
print(estudiantes.values())

#imprimir los items
print(estudiantes.items())

#recorrer un diccionario
for clave, valor in estudiantes.items():
    print(clave, valor)

