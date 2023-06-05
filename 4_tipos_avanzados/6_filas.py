#COLECTION PARA FIFO (first in, first out) FILAS
from collections import deque

fila= deque([1,2])
fila.append(3)
fila.append(4)
fila.append(5)

print(fila)

#REMOVIENDO EL PRIMER ELEMENTO
fila.popleft()
fila.popleft()
print(fila)

#EVALUANDO FILA VACIA O SÍ ES O NO UNA LISTA
if not fila:
    print("fila vacia")