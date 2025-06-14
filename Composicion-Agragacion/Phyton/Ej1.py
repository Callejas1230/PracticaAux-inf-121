class Habitacion:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

    def mostrar_info(self):
        return "Habitación: " + self.nombre + ", Tamaño: " + str(self.tamaño) + " m²"

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_casa(self):
        print("Dirección: " + self.direccion)
        print("Habitaciones:")
        for h in self.habitaciones:
            print(h.mostrar_info())

hab1 = Habitacion("Sala", 40)
hab2 = Habitacion("Cocina", 20)
hab3 = Habitacion("Dormitorio", 10)
hab4 = Habitacion("Baño", 8)

mi_casa = Casa("Av. Hernando Siles")
mi_casa.agregar_habitacion(hab1)
mi_casa.agregar_habitacion(hab2)
mi_casa.agregar_habitacion(hab3)
mi_casa.agregar_habitacion(hab4)

mi_casa.mostrar_casa()