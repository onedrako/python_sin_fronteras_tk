from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")

vertical = Scale(root, from_=0, to=200, command=lambda x: enviar())
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

def enviar():
  hor = horizontal.get()
  ver = vertical.get()
  print (hor, ver)

btn = Button(root, text="Click Me!", command=enviar).pack()

root.mainloop()
