class Mascota:

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print("Guau Guau")
        elif self.especie.lower() == "gato":
            print("Miau Miau")
        else:
            print("La mascota hace un sonido.")
