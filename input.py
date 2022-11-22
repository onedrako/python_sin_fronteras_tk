from tkinter import *

root = Tk()
root.title("Hola Mundo")
root.geometry("500x500")  #tamaño de ventana (anchoxalto)

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Escribe tu nombre: ")

def click():
    hello =  e.get()
    # myLabel = Label(root, text="Hola " + hello)
    # myLabel.pack()
    # myLabel.configure(text="Hola " + hello)
    l.configure(text=hello)
    e.delete(0, END)

btn = Button(root, text="Click me", padx=50, pady=50, command=click)
btn.pack()

l = Label(root, text="Texto de la etiqueta")
l.pack()


root.mainloop()
