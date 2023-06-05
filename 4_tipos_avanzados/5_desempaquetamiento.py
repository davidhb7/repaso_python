#IMPRIMI ITERABLES SIN CORCHETES O PARENTESIS
lista=[1,2,3,4,5]
print(lista)#CON CORCHETES
print(*lista)#SIN CORCHETES


##DESEMPAQUETANDO DICCIONARIOS
diccionario1= {"perro":1, "gato":2, "loro":3}
diccionario2={"chawisque":4, "mamalona":5}
uionDic={**diccionario1, **diccionario2}
print(uionDic)
print(*uionDic)