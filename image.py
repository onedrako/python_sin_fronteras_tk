from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image")
root.geometry("500x500")  #tamaño de ventana (anchoxalto)

# image = Image.open("./pic.jpg")
# image.show()

img = ImageTk.PhotoImage(Image.open("./pic.jpg"))
l = Label(image=img)
l.pack() 

root.mainloop()