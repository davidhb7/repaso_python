edad = 25

##IF NORMAL
if edad>18:
    print("sisa")
    if edad>20:
        print("tines descuento")
elif edad>35:
    print("acumula puntos?")
else:
    print("no cumples con la edad minima")

##IF RESUMIDO
if 18<=edad<=50:
    print("rango establecido")


##OPERADOR TERNARIO
exp=7
mensaje= "senior" if exp>10 else "es mid"
print(mensaje)
