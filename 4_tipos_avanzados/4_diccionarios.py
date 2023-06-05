#ESTRUCTURA DE ARREGLO TIPO LLAVE-VALOR. SE TRABAJA CON CORCHETES

diccionario = {"x":7, "y":11 }
print(diccionario["x"])
print(diccionario["y"])
#AGREGANDO VALORES Y LLAVES
diccionario["z"]=21
#ACCEDER AL DICCIONARIO
print(diccionario.get("x"))

#SI NO EXISTE, PASAR VALOR POR DEFECTO
print(diccionario.get("a", 1))
print(diccionario)

#ELIMINAR VALOR
del diccionario["x"]
del (diccionario["y"])

##FORMAS DE RECORRER DICCIONARIO
for valor in diccionario:
    print(valor,":",diccionario[valor]) 
    

for i,j in diccionario.items():
    print(i,j)


usuarios= [
    {"id":1, "nombre": "David"},
    {"id":2, "nombre": "Tania"},
    {"id":3, "nombre": "Joelito"},
    {"id":4, "nombre": "Amaru"},
    ]


#RECORRIENDO UN LISTA DE DICCIONARIOS
for usuario in usuarios:
     print(usuario["nombre"])