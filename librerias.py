# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import time

n = 1000

#Lista en python

l1 = list(range(n))
l2 = list(range(n))

start = time.time()
l3 = []
for x in range(len(l1)):
    l3.append(l1[x] + l2[x])
end = time.time()
print('Total milisegundos lista:', (end - start) * 1000)

n1 = np.arange(n)
n2 = np.arange(n)

start = time.time()
n3 = n1 + n2
end = time.time()

print('Total milisegundos numpy:', (end - start) * 1000)

# Metodos de numpy

a = [2, 3, 4, 5, 6]
b = [7, 9, 10, 11, 12]

# Convertir el vector en un vector numpy

n1 = np.array(a)
n2 = np.array(b)

# Operaciones numpy

n3 = n1 + n2
n3 = n1 - n2
n3 = n1 * n2
n3 = n1 / n2

# Conocer las dimensiones de un vector numpy

n3.shape

na = np.array([[3, 4, 5], [5, 6, 7], [5, 6, 7]])

# Matriz de ceros

n4 = np.zeros((4, 4))

# Matriz de unos

n4 = np.ones((4, 4))

# Matriz de un numero especifico

n4 = np.full((5,6),9)

# Matriz con elementos random

n4 = np.random.random((3, 3))

# Matriz identidad

n4 = np.eye(5)

# Algoritmo que da como resultado la diagonal principal de una matriz  random
#y los demas elementos cero

n4 = np.random.random((4,4))
print(n4)
n5 = np.eye(4)
print(n5)
n6 = n4 * n5
print(n6)
print(n4.max())
print(n4.min())
print(n4.mean())
print(n4.sum())
print(np.sqrt(n4))
print(np.sin(n4))
print(np.cos(n4))
print(np.log(n4))

f1 = [4, 5, 6, 7, 9]
f2 = [3, 4, 5, 6, 8]
f3 = [1, 5, 6, 9, 10]

matriz = np.array([f1, f2, f3])
transp = matriz.T

c = [[3, 1, 9],[7, 2, 4], [8, 6, 6]]
d = [[3, 1, 9],[7, 2, 4], [8, 6, 6]]

nc = np.array(c)
nd = np.array(d)

# Validar que sean iguales

nc == nd

# Multiplicar por un escalar

nc * 2

# Elevear ak cuadrado

nc ** 2

# Filtrado de elementos

nc[nc < 5]

# Fila uno todas las columnas

nc[1, :]

# Todas las filas de la columna uno

nc[:, 1]

nc[2, 1:2]

nc[2, 1:3]

nc[2, 1:]

# Matriz aleatoria de numeros enteros

ma = np.random.randint(20, size=(5,5))

# Random de numeros decimales

ma = np.random.uniform(0,5, size=(5,5))

# Haga un algoritmo que dada una matriz aleatoria de 49 calificaciones indique
# cuales se encuentren por encima del promedio del salon

notas = np.random.uniform(0,5, size=(7,7))

promedio = notas.mean()

aux = notas[notas > promedio]

print(notas)
print(f'El promedio es: {promedio}')
print(f'Las calificaciones buscadas son: {aux}')






































