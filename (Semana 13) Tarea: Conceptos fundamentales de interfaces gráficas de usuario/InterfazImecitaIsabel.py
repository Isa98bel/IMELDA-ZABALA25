import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")

# Funcionalidades de los botones
def agregar():
    item = entry_texto.get()
    if item:  # Verifica si el campo de texto no está vacío
        lista.insert(tk.END, item)
        entry_texto.delete(0, tk.END)  # Limpia el campo de texto

def limpiar():
    lista.delete(0, tk.END)

# Componentes GUI
entry_texto = tk.Entry(root, width=50)
entry_texto.pack()

boton_agregar = tk.Button(root, text="Agregar", command=agregar)
boton_agregar.pack()

boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar)
boton_limpiar.pack()

lista = tk.Listbox(root, width=50)
lista.pack()

# Añadir texto con el nombre al final
nombre_label = tk.Label(root, text="IMELDA ZABALA")
nombre_label.pack()

# Ejecutar la aplicación
root.mainloop()
