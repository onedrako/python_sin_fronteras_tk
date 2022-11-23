from tkinter import *

root = Tk()
root.title("Checkboxes")

root.geometry("500x500")

var = StringVar()
var.set("chanchito feliz")

c = Checkbutton(root, text="Soy un checkbox", variable=var, onvalue="Si", offvalue="chanchito feliz")
c.pack()

def mostrar():
  l = Label(root, text=var.get()).pack()

btn = Button(root, text="Click Me!", command=mostrar).pack()

root.mainloop()