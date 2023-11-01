class Vehiculo:
    def __init__(self, marca, modelo, placa, color):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.color = color

    def obtener_informacion(self):
        return f"Marca: {self.marca}\n Modelo: {self.modelo}\n Placa: {self.placa}\n Color: {self.color}"

class Autobus(Vehiculo):
    def __init__(self, marca, modelo, placa, color, capacidad_pasajeros):
        super().__init__(marca, modelo, placa, color)
        self.capacidad_pasajeros = capacidad_pasajeros

    def obtener_informacion(self):
        informacion = super().obtener_informacion()
        return f"{informacion}\n Capacidad de Pasajeros: {self.capacidad_pasajeros}"

class Taxi(Vehiculo):
    def __init__(self, marca, modelo, placa, color, licencia):
        super().__init__(marca, modelo, placa, color)
        self.licencia = licencia

    def obtener_informacion(self):
        informacion = super().obtener_informacion()
        return f"{informacion}\n Licencia: {self.licencia}"
    