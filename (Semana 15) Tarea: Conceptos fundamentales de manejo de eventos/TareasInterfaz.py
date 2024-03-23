import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import font as tkFont
from tkinter import messagebox

class PersonalAgendaApp:
    def __init__(self, root):
        self.root = root
        root.title("Agenda Personal")

        # Configuración de frames
        self.frame_treeview = tk.Frame(root)
        self.frame_treeview.pack(fill=tk.BOTH, expand=True)

        self.frame_entry = tk.Frame(root)
        self.frame_entry.pack(fill=tk.X)

        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(fill=tk.X)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_treeview, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # DatePicker para la fecha
        tk.Label(self.frame_entry, text="Fecha:").pack(side=tk.LEFT, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entry, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Combobox para la hora
        tk.Label(self.frame_entry, text="Hora:").pack(side=tk.LEFT, padx=5, pady=5)
        self.hora_entry = ttk.Combobox(self.frame_entry, width=10, values=[f"{h:02d}:00" for h in range(24)] + [f"{h:02d}:30" for h in range(24)])
        self.hora_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Entrada para la descripción
        tk.Label(self.frame_entry, text="Descripción:").pack(side=tk.LEFT, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(self.frame_entry)
        self.descripcion_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Botones para agregar, marcar como completado, eliminar eventos y salir
        self.btn_agregar = tk.Button(self.frame_buttons, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_completar = tk.Button(self.frame_buttons, text="Marcar Evento Como Completado", command=self.marcar_completado)
        self.btn_completar.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_eliminar = tk.Button(self.frame_buttons, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_salir = tk.Button(self.frame_buttons, text="Salir", command=root.quit)
        self.btn_salir.pack(side=tk.RIGHT, padx=5, pady=5)

        # Créditos
        creditos_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        self.label_creditos = tk.Label(root, text="Elaborado por: ISABEL ZABALA", font=creditos_font, fg="black")
        self.label_creditos.pack(side=tk.BOTTOM, fill=tk.X)

    def agregar_evento(self):
        # Agrega un nuevo evento con los datos proporcionados
        fecha = self.fecha_entry.get_date().strftime("%Y-%m-%d")
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()
        if fecha and hora and descripcion:
            self.tree.insert('', tk.END, values=(fecha, hora, descripcion))
            self.fecha_entry.set_date(datetime.today())
            self.hora_entry.set('')
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos para agregar un evento.")

    def marcar_completado(self):
        # Marca el evento seleccionado como completado
        seleccionado = self.tree.selection()
        for i in seleccionado:
            valores = self.tree.item(i, 'values')
            nueva_descripcion = f"[Completado] {valores[2]}"
            self.tree.item(i, values=(valores[0], valores[1], nueva_descripcion))

    def eliminar_evento(self):
        # Elimina el evento seleccionado
        seleccionado = self.tree.selection()
        if seleccionado:
            for i in seleccionado:
                self.tree.delete(i)
        else:
            messagebox.showinfo("Información", "Selecciona un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalAgendaApp(root)
    root.mainloop()
