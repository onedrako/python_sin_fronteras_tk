from tkinter import *

root = Tk()
root.title("Pies a metros")
root.geometry("500x500")  #tamaño de ventana (anchoxalto)

def calcular(*args):
  try:
    value = float(pies.get())
    m = int(value * 0.3048 * 10000.0 + 0.5)/10000.0 
    metros.set(m)
  except ValueError:
    metros.set("ERROR")

frame = Frame(root, pady=3, padx=12)
frame.grid(row=0, column=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)
pies_input.grid(row=0, column=1)

metros = StringVar()
Label(frame, textvariable=metros).grid(row=1, column=1)

Button(frame, text="Calcular", command=calcular).grid(row=2, column=2)
Label(frame, text="Pies").grid(row=0, column=0)
Label(frame, text="Es igual a").grid(row=1, column=0)
Label(frame, text="metros").grid(row=1, column=2)

pies_input.focus()
root.bind("<Return>", calcular)
root.mainloop()