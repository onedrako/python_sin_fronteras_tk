from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hola Mundo")

# def click():
#     messagebox.showwarning("Advertencia", "Esto es una advertencia")

# def click():
#     messagebox.showinfo("Info", "Esto es información")
# def click():
#     messagebox.showerror("error", "Esto es Error")

# def click():
#     respuesta = messagebox.askquestion("Pregunta", "¿Estas seguro de salir?")
#     print(respuesta)
#     if respuesta == "yes":
#         messagebox.showinfo("Respuesta", "La respuesta fue " + respuesta)
#     else:
#         messagebox.showinfo("Respuesta", ":( La respuesta fue " + respuesta)


# def click():
#     respuesta = messagebox.askokcancel("Pregunta", "Desea realizar acción?")
#     if respuesta:
#         messagebox.showinfo("Respuesta", "La respuesta fue " + str(respuesta))
#     else:
#         messagebox.showinfo("Respuesta", ":( La respuesta fue " + str(respuesta))

def click():
    respuesta = messagebox.askyesno("Pregunta", "Desea realizar acción?")
    if respuesta:
        messagebox.showinfo("Respuesta", "La respuesta fue " + str(respuesta))
    else:
        messagebox.showinfo("Respuesta", ":( La respuesta fue " + str(respuesta))


btn = Button(root, text="Presiona", command=click)
btn.pack()

root.mainloop()