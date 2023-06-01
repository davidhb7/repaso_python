#LISTAS CORCHETES
lista = [1,2,3]

#MATRIZ
matriz = [[1,2,], [3,4], [5,6]]
print((matriz))

#MANIPULANDO LISTAS
visajes = ["sable", "tote", "perez", "caleto", "billullo", "perez"]
visajes[0]#ACCEDIENDO AL VALOR
visajes[0]="xyz"#CAMBIANDO VALOR
visajes[0:2] #RANGO 0, 1 Y 2 

#ITERANDO LA LISTA CON EL INDICE
for visaje in enumerate(visajes):#CON ESE METODO, IMPRIME LA LISTA EN TUPLA
    print(visaje)
    

#BUSCANDO POR INDICE
if "vicha" in visajes:
    print(visajes.index("tote"))
else:
    print("No esta mi socio")

#CONTANDO ELEMENTOS DE LA LISTA
print(visajes.count("perez"))

#AGREGANDO A LA LISTA
visajes.insert(7, "color")
print(visajes)
visajes.append("chuzo")#METODO AGREGA AL FINAL
print(visajes)

#ELIMINANDO 
visajes.remove("perez")
print(visajes)
visajes.pop()#ELIMINA EL ULTIMO CUANDO NO SE PONE EL INDICE COMO ARGUMENTO
print(visajes)
del visajes[3]#ELIMINAR POR INDICE CON PALABRA RESERVADA
print(visajes)


#ORDENANDO LISTA
visajes.sort()
print(visajes)
visajes.sort(reverse=True)#DE ATRAS PARA ADELANTE
print(visajes)

#ORDENANDO LISTA COMPLEJA
#genteMex = [[5,"Chalino"], [2,"Chapito"], [9,"Chino"]]
genteMex = [["Lazca",5], ["Chapito",2], ["Chino",9]]
genteMex.sort()
print(genteMex)

#ORDENANDO POR KEY
def ordena(elemento):
    return elemento[1]#cero es el nombre. 1 es el numero. poner el indice del arreglo porel cual se desea ordenar

genteMex.sort(key=ordena)
print(genteMex)

#USANDO LAMBDA
genteMex.sort(key=lambda elemento: elemento[0])
print(genteMex)