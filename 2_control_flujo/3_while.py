numero=1
while numero < 100:
    print(numero)
    numero*=2

comando= ""
while comando.lower() != "salir":
    comando=input("$ ")
    print(comando)


##ANIDADO
for i in range(3):
    for j in range(2):
        print(f"{i},{j}")