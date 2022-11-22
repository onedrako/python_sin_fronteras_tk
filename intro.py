from tkinter import *

root = Tk()
root.title("hola mundo")  #titulo
root.geometry("500x500")  #tamaño de ventana (anchoxalto)

# label = Label(root, text="Hola Mundo!, mi primera etiqueta") #(donde renderiza y el texto)
# label.pack() # Para mostrarla al usuario, hacerla visible

# label = Label(root, text="Hola Mundo!, mi primera etiqueta").pack()
# otra forma de llamarlo

l1 = Label(root, text="Hola Mundo!, mi primera etiqueta")
l2 = Label(root, text="Adios Mundo!, mi segunda etiqueta")
l3 = Label(root, text="")
l1.grid(row=0, column=0)
l3.grid(row=1, column=1)
l2.grid(row=10, column=10)

root.mainloop()

