import tkinter as tk
import os
from tkinter import messagebox
from vehiculo import *

def mostrar_informacion_vehiculo(vehiculo):
    info_vehiculo = vehiculo.obtener_informacion()
    messagebox.showinfo("Información del Vehículo", info_vehiculo)

def mostrar_imagen_vehiculo(vehiculo):
    ventana_imagen = tk.Toplevel()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    imagen_path = os.path.join(script_directory, f"imagenes/{vehiculo.__class__.__name__.lower()}.png")
    imagen = tk.PhotoImage(file=imagen_path)
    label = tk.Label(ventana_imagen, image=imagen)
    label.image = imagen
    label.pack()
    ventana_imagen.mainloop()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Transporte Urbano")

ventana.geometry("600x400")

autobus = Autobus("Mercedes-Benz", "Sprinter", "ABC-123", "Amarillo", 30)
taxi = Taxi("Toyota", "Corolla", "XYZ-789", "Blanco", "12345")

boton_info_autobus = tk.Button(ventana, text="Info Autobus", command=lambda: mostrar_informacion_vehiculo(autobus))

boton_imagen_autobus = tk.Button(ventana, text="Imagen Autobus", command=lambda: mostrar_imagen_vehiculo(autobus))

boton_info_taxi = tk.Button(ventana, text="Info Taxi", command=lambda: mostrar_informacion_vehiculo(taxi))

boton_imagen_taxi = tk.Button(ventana, text="Imagen Taxi", command=lambda: mostrar_imagen_vehiculo(taxi))

boton_info_autobus.pack()
boton_imagen_autobus.pack()
boton_info_taxi.pack()
boton_imagen_taxi.pack()

ventana.mainloop()
