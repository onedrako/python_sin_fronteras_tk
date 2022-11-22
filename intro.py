from tkinter import *

root = Tk()
root.title("hola mundo")  #titulo
root.geometry("500x500")  #tamaño de ventana (anchoxalto)

label = Label(root, text="Hola Mundo!, mi primera etiqueta") #(donde renderiza y el texto)
label.pack() # Para mostrarla al usuario, hacerla visible

# label = Label(root, text="Hola Mundo!, mi primera etiqueta").pack()
# otra forma de llamarlo

root.mainloop()