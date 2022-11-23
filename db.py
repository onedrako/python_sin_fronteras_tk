from tkinter import *
import sqlite3

root = Tk()
root.title("Hola Mundo: todo list")
root.geometry("500x500")

conn = sqlite3.connect("todo.db")
c = conn.cursor() #con este se realizan las tareas/consultas
c.execute("""CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT NOT NULL,
    completed BOOLEAN NOT NULL
    );
""")

conn.commit()

def addTodo():
    todo = e.get()
    c.execute("""
      INSERT INTO todo (description, completed) VALUES (?, ?)
    """, (todo, False))
    conn.commit()
    e.delete(0, END)

l = Label(root, text="tarea")
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text="Agregar", command=addTodo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text="Mis Tareas", padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=5)

e.focus()

root.bind("<Return>", lambda x: addTodo())

root.mainloop()