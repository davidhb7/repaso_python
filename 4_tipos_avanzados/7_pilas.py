#PILAS (Last in, Firts ut)
pila=[]

pila.append(1)
pila.append(2)
pila.append(3)

print(pila)

pila.pop()#ELIMINA EL ULTIMO ELEMENTO

print(pila)


if not pila:
    print("Pila vacia")