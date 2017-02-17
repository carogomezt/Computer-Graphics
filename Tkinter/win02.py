#win02.py
from Tkinter import *

if __name__ == '__main__':
    ventana = Tk()
    et1 = Label(ventana, text="Numero 1: ")
    et1.grid(row=1, column=1)
    en1 = Entry(ventana, width=10)
    en1.grid(row=1, column=2)
    et2 = Label(ventana, text="Numero 2: ")
    et2.grid(row=2, column=1)
    en2 = Entry(ventana, width=10)
    en2.grid(row=2, column=2)
    ventana.mainloop()
