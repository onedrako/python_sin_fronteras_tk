from tkinter import *
from tkinter import messagebox # messagebox es un módulo de tkinter
from tkinter import ttk # Para usar Treeview
import sqlite3 # Para usar sql

root = Tk()
root.title("Hola Mundo: CRM")

conn = sqlite3.connect('crm.db')

c = conn.cursor()
c.execute("""
  CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    empresa TEXT NOT NULL
  );
""")

def render_clientes():
  rows = c.execute("SELECT * FROM cliente").fetchall()

  tree.delete(*tree.get_children())

  for row in rows:
    tree.insert("", END, row[0], values=(row[1], row[2], row[3])  )

def insertar(cliente):
  c.execute("""
    INSERT INTO cliente (nombre, telefono, empresa) VALUES (?, ?, ?)
  """, (cliente['nombre'], cliente['telefono'], cliente['empresa']))
  conn.commit()
  render_clientes()

def nuevo_cliente():
  def guardar():
    if not nombre.get():
      messagebox.showerror("Error", "El campo nombre es obligatorio")
      return
    if not telefono.get():
      messagebox.showerror("Error", "El campo teléfono es obligatorio")
      return
    if not empresa.get():
      messagebox.showerror("Error", "El campo empresa es obligatorio")
      return

    cliente = {
      'nombre': nombre.get(),
      'telefono': telefono.get(),
      'empresa': empresa.get()
    }
    insertar(cliente)
    top.destroy()

  top = Toplevel()
  top.title("Nuevo Cliente")

  lnombre = Label(top, text="Nombre")
  nombre = Entry(top, width=40)
  lnombre.grid(row=0, column=0, padx=5, pady=5)
  nombre.grid(row=0, column=1, padx=5, pady=5)

  ltelefono = Label(top, text="Telefono")
  telefono = Entry(top, width=40)
  ltelefono.grid(row=1, column=0, padx=5, pady=5)
  telefono.grid(row=1, column=1, padx=5, pady=5)
    
  lempresa = Label(top, text="Empresa")
  empresa = Entry(top, width=40)
  lempresa.grid(row=2, column=0, padx=5, pady=5)
  empresa.grid(row=2, column=1, padx=5, pady=5)

  guardar = Button(top, text="Guardar", command=guardar)
  guardar.grid(row=3, column=1, padx=5, pady=5)

  top.mainloop()

def eliminar_cliente():
  id = tree.selection()[0] #Obtenemos un listado de los id´s de la fila

  cliente = c.execute("SELECT * FROM cliente WHERE id = ?", (id,)).fetchone()
  respuesta = messagebox.askokcancel("Eliminar", "¿Estás seguro de eliminar el cliente " + cliente[1] + " ?")
  if respuesta:
    c.execute("DELETE FROM cliente WHERE id = ?", (id,))
    conn.commit()
    render_clientes()
  else:
    pass

btn = Button(root, text="Nuevo Cliente", command=nuevo_cliente)
btn.grid(column=0, row=0)

btn_eliminar = Button(root, text="Eliminar Cliente", command=eliminar_cliente)
btn_eliminar.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree["columns"] = ("Nombre", "Telefono", "Empresa")
tree.column("#0", width=0, stretch=NO)
tree.column("Nombre")
tree.column("Telefono")
tree.column("Empresa")

tree.heading("#0", text="")
tree.heading("Nombre", text="Nombre")
tree.heading("Telefono", text="Telefono")
tree.heading("Empresa", text="Empresa")

tree.grid(column=0, row=1, columnspan=2)

render_clientes()

root.mainloop()
