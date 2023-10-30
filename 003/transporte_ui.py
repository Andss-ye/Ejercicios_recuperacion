import tkinter as tk
from PIL import Image, ImageTk

class TransporteUI:
    def __init__(self, transporte, mostrar_info_callback):
        self.transporte = transporte
        self.mostrar_info_callback = mostrar_info_callback

        self.frame = tk.Frame()
        self.button = tk.Button(self.frame, text=transporte.tipo, command=self.mostrar_info)
        self.button.pack()

    def mostrar_info(self):
        self.mostrar_info_callback(self.transporte)

def crear_ventana():
    root = tk.Tk()
    root.title("Medios de Transporte Urbano")
    return root

def crear_widgets(root):
    imagen_label = tk.Label(root)
    info_label = tk.Label(root, text="", font=("Arial", 12))
    imagen_label.pack()
    info_label.pack()
    return imagen_label, info_label

def iniciar_aplicacion(root):
    root.mainloop()
