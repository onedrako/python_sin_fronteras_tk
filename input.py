from tkinter import *

root = Tk()
root.title("Hola Mundo")
root.geometry("500x500")  #tamaño de ventana (anchoxalto)

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Escribe tu nombre: ")

def click():
    texto =  e.get()
    textVariable.set(texto)
    valor = textVariable.get()
    print(valor)
    # myLabel = Label(root, text="Hola " + hello)
    # myLabel.pack()
    # myLabel.configure(text="Hola " + hello)
    # l.configure(text=hello)
    e.delete(0, END)

btn = Button(root, text="Click me", padx=50, pady=50, command=click)
btn.pack()

textVariable = StringVar()
 

l = Label(root, textvariable=textVariable)
l.pack()


root.mainloop()
