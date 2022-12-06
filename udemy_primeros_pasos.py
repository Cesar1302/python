# Acá va a un comentario
if 3 > 5: # Acá va a un comentario
    print('Esto no se va a imprimir')

# if 5 > 3: # Acá va otro comentario
    # print('5 es mayor a 3')


x = 5
y = 'chanchito feliz'

print(x, y)

correo = 'chanchito@feliz.com'

print(correo)

_mi_var = 'chanchito'
MIVAR = 'chanchito'
a, b, c = 'Lala', 'Lele', 'Lili'

# print(a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'

# print(valor1, valor2, valor3)

inicio = 'Hola'
final = 'mundo'

# print(inicio + final)

palabra = 'hola mundo' # string, se usan las comillas simples para solo anotar texto (string)
oracion = "hola mundo comilla doble" # string, tambien se pueden definir los strings con comilla doble

entero = 20 # integer
conDecimales = 20.2 # float
complejo = 1j # para usar numeros complejos, los numeros deben de contener una "j" al final.

# print(palabra, oracion, entero, conDecimales, complejo)

lista = ['Hola', 'Mundo', 'Chanchito feliz'] # para una lista se debe hacer usando los corchetes.
lista2 = lista.copy()
lista.append('Chanchito triste')
# lista.clear()
# print(lista, lista2.count(3))
# print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista, largoLista2)

# print(lista[2])

# lista.pop() # este elimina el último elemento de la lista
# lista.remove('Hola') # este elimina un elemento por su valor

lista.reverse()
lista.sort()
tupla = ('hola', 'mundo', 'somos', 'tupla') # para usar tuplas debemos usar parentesis, estos datos no pueden ser modificados.
listaDeTupla = list(tupla)
listaDeTupla.append('chanchito')
# print(listaDeTupla)

rango = range(6)
# print(rango)

diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])
# print(diccionario.get('nombre'))
diccionario['nombre'] = 'Fluffy'

# print(len(diccionario))

diccionario['ronronea'] = 'Si'

# print(diccionario)
# diccionario.pop('ronronea')
# diccionario.popitem()
# copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario)
# del diccionario['ronronea']
diccionario.clear()
# print(diccionario, copiaGatito)

fluffy = {
    "nombre": "Fluffy",
    "edad": 4
} # Los diccionarios deben esta entre llaves

mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6)
print(perritos)

verdadero = True
falso = False

print(verdadero, falso)


# i = 0

# while i < 5 :
#     i += 1
#     if i == 3:
#         continue
#     print(i)