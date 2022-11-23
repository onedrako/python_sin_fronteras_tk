from tkinter import *

root = Tk()
root.title("Option Menu")

def enviar():
  l = Label(root, text=value.get()).pack()
  l.pack()

lista = ["Chanchito Feliz", "Chanchito Triste", "Chanchito Enojado"]
value = StringVar()
value.set(lista[0])


drop = OptionMenu(root, value, *lista).pack()

btn = Button(root, text="Enviar", command=enviar).pack()

root.mainloop()