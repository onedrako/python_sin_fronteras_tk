from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Archivo")

# root.filename = filedialog.askopenfilename(title="Elige una foto", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
# l = Label(root, text=root.filename).pack()

# img = ImageTk.PhotoImage(Image.open(root.filename))
# imgtk = Label(root, image=img).pack()

def open():
  global imgtk
  root.filename = filedialog.askopenfilename(title="Elige una foto", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
  l = Label(root, text=root.filename).pack()

  img = Image.open(root.filename)
  imgtk = ImageTk.PhotoImage(img)

  l2 = Label(root, image=imgtk).pack()


btn = Button(root, text="Abrir", command=open).pack()

root.mainloop()