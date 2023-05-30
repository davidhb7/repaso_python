print("Bienvenidoa a la calculadora...")
n1=int(input("Ingrese primer numero: "))
n2=int(input("Ingrese segundo numero: "))

sum=n1+n2
res=n1-n2
div=n1/n2
mul=n1*n2
comando=""

while comando != "salir":
    print("Digite la operacion: sum, res, div o mul:")
    comando=input("$ ")
    if comando == "sum":
        print(f"La suma entre {n1}, {n2} es igual: ",sum)
    elif comando == "res":
        print(f"La resta entre {n1}, {n2} es igual: ",res)
    elif comando == "div":
        print(f"La division entre {n1}, {n2} es igual: ",div)
    elif comando == "mul":
        print(f"La multiplicacion entre {n1}, {n2} es igual: ",mul)
    elif comando == "salir":
        print("Saliendo de la calculadora...")
    else:
        print("Operacion inexistente...")
