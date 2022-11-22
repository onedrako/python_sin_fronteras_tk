from tkinter import *

root = Tk()
root.title("Hola Mundo")
root.geometry("500x500")  #tamaño de ventana (anchoxalto)

# frame = LabelFrame(root, text="Login", padx=10, pady=10, borderwidth=10)
frame = LabelFrame(root, padx=10, pady=10, borderwidth=10)
frame.pack()
# frame2.pack()


l = Label(frame, text="Estoy dentro de un frame!")
btn = Button(frame, text="Salir", padx=50, pady=50, command=root.quit)
l.pack()
btn.pack()


root.mainloop()
