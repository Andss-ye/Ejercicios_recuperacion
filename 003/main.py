import tkinter as tk
from transporte_urbano import TransporteUrbano
from transporte_ui import TransporteUI, crear_ventana, crear_widgets, iniciar_aplicacion

# Crear instancias de TransporteUrbano
autobus = TransporteUrbano("Autobús", "Mercedes-Benz", "Sprinter", 50, "autobus.png")
metro = TransporteUrbano("Metro", "Alstom", "MP 05", 500, "metro.png")

# Función para mostrar información y la imagen
def mostrar_info(transporte):
    info_label.config(text=transporte.mostrar_informacion())
    imagen_label.config(image=ImageTk.PhotoImage(transporte.imagen))
    imagen_label.photo = transporte.imagen

root = crear_ventana()
imagen_label, info_label = crear_widgets(root)

# Crear instancias de la interfaz de usuario para cada medio de transporte
autobus_ui = TransporteUI(autobus, mostrar_info)
metro_ui = TransporteUI(metro, mostrar_info)

# Iniciar la aplicación
iniciar_aplicacion(root)
