def hablalo(nombre):
    print(f"bien o no, {nombre}")
    print("menorcito")

hablalo("fulano")


##PARAMETRO POR DEFECTO
def hablalo2(nombre, apellido="detal"):
    print(f"bien o no, {nombre} {apellido}")
    print("menorcito")

hablalo2("fulano")


##PARAMETRO NOMBRADOS
def hablalo3(nombre, apellido="detal"):
    print(f"bien o no, {nombre} {apellido}")
    print("menorcito")

hablalo3(apellido="corleone",nombre="pepe")##para identificar el orden y pertenencia de los argumentos