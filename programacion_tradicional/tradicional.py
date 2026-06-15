# Programa tradicional utilizando funciones

def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie: ")
    edad = input("Ingrese la edad: ")

    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }

    return mascota


def mostrar_mascota(mascota):
    print("\nInformación de la mascota")
    print("Nombre:", mascota["nombre"])
    print("Especie:", mascota["especie"])
    print("Edad:", mascota["edad"])


def main():
    mascota = registrar_mascota()
    mostrar_mascota(mascota)


if __name__ == "__main__":
    main()
