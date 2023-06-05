mensaje="hola mano"
print(type(mensaje))#VER EL TIPO PRIMITIVO

#CLASE: El molde o plano
#OBJETO: es la instancia de una clase, que es creado a partir del molde

class Perro:
    patas = 4
    #CONSTRUCTOR
    #SELF, hace referencia al instancia(objeto) que se crea 
    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad
        
    #PRIMER PARAMETRO, SIEMPE ES self
    def ladra(self):#SE LES LLAMA METODOS CUANDO SON PARTE DE UNA CLASE.
        print(f"{self.nombre} dice: pevepe o que?")
        
        

        
        

def aleatorio(): #SE LES LLAMA FUNCIONES, NO SON PARTE DE UNA CLASE
    print("Descripcion de funcion")
    
    
mi_perro = Perro("Pepe", 9)
mi_perro2 = Perro("Chabelo", 9)
print(type(mi_perro))
print(mi_perro.ladra())
mi_perro.ladra()

#VER SI PERTENECE A UNA INSTANCIA O NO
print(isinstance(mi_perro, Perro))
print()
mi_perro2.__init__("Cuki", 10)

mi_perro2.ladra()
print(Perro.patas)
print(mi_perro.patas)
