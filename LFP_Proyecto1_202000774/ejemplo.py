from tkinter import *
from tkinter import ttk

#root = Tk()
#ttk.Button(root, text="Hello World").grid()
#root.mainloop()
"""
class tkinter:
    def __init__(self) -> None:
        self.ventana = Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
        self.frame = ttk.Frame(self.ventana, padding=10)
        self.frame.grid()
        self.label = ttk.Label(self.frame, text="Hola Mundo").grid(column=0, row = 0)
        self.salir = ttk.Button(self.frame, text="Quit", command=self.ventana.destroy).grid()
        self.ventana.mainloop()

root = tkinter()

class Test:
    
    __egg = 7

p = Test()
print(p._Test__egg)

lista = ["a", "b", "c", "d", "e", "f"]

def retorno():

    return "a" , "b", "c"

def buscar():
    j = retorno()
    print(j[1])

buscar()
"""
i = 4
j = 5
hola = f''' {i} hola {j} '''



k = 0
while k <= len(hola)-1:
    char = hola[k]
    print(k)
    k+=1