class Perro:
    patas = 4

    # CONSTRUCTOR
    # SELF, hace referencia al instancia(objeto) que se crea
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # PRIMER PARAMETRO, SIEMPE ES self
    def ladra(self):  # SE LES LLAMA METODOS CUANDO SON PARTE DE UNA CLASE.
        print(f"{self.nombre} dice: pevepe o que?")

