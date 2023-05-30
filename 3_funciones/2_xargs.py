#SENCILLO
def sum(a, b):
    print(a + b)

sum(2,3)

#CUALQUIER CANTIDAD DE ARGUMENTOS
def sum2(*numeros):
    resultado=0
    for num in numeros:
        resultado+= num
    print(resultado)

sum2(3,4, 5,7)