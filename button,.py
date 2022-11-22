from tkinter import *

root = Tk()
root.geometry("500x500")  #tamaño de ventana (anchoxalto)


l = Label(root, text="Hola Mundo")
def click():
  l.pack()

btn = Button(root, text="Click", command=click, fg="white", bg="black")
btn.pack()

root.mainloop()

