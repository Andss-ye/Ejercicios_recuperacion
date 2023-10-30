from PIL import Image

class TransporteUrbano:
    def __init__(self, tipo, marca, modelo, capacidad_pasajeros, imagen_path):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.imagen = Image.open(imagen_path)

    def mostrar_informacion(self):
        info = f"Tipo: {self.tipo}\nMarca: {self.marca}\nModelo: {self.modelo}\nCapacidad de Pasajeros: {self.capacidad_pasajeros}"
        return info
