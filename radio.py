from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hola Mundo")

r = IntVar()
r.set("2")

CHANCHITOS = [
    ("Feliz", "Feliz"),
    ("Triste", "Triste"),
    ("Enojado", "Enojado"),
    ("Dormido", "Dormido"),
]

chanchito = StringVar()
chanchito.set("lala")

for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()

# Radiobutton(root, text="Opción 1", variable=r, value=1).pack()
# Radiobutton(root, text="Opción 2", variable=r, value=2).pack()

l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()