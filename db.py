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