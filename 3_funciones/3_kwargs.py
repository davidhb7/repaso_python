#EMPAQUETRA TODOS ARGUMENTOS LOS INGRESADOS EN 1 PARAMETRO
#KEY WORD ARGUMENT**
def get_product(**datos):
    print(datos["id"], datos["visaje"])#especifica por la key los datos deseados

get_product(id="23", name="fulano", visaje="sable")#Arroja un diccionario

#CUANDO SE USA RETURN, EL METODO DEBE GUARDARSE EN UNA VARIABLE E IMPRIMIRSE