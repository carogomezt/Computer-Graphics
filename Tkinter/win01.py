#win01.py
from Tkinter import *

def Mostrar():
    valor = etxt.get()
    etq2 = Label(ventana, text ="digitado" + valor)
    etq2.pack()

if __name__ == '__main__':
    ventana = Tk()
    ventana.title('ejemplo')
    etq = Label(ventana, text = "Ejemplo de etiqueta")
    etxt = Entry(ventana)
    btn = Button(ventana, text="Aceptar", command = Mostrar)
    etq2 = Label(ventana, text="digitado: ")
    etq.pack()
    etxt.pack()
    btn.pack()
    etq2.pack()
    ventana.mainloop()
