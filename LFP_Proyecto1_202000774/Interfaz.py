from fileinput import filename
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
from Analizador_Lexico import Analizador

class Interfaz:
    def __init__(self):
        self.pantalla_principal = Tk()
        self.pantalla_principal.title("Pantalla Principal Proyecto 1")
        self.pantalla_principal.config(background="#04293A")
        #print(self.pantalla_principal.configure().keys())
        self.pantalla_principal.geometry("1000x600")
        self.pantalla_principal.resizable(0,0)
        self.frame()

    def frame(self):
        self.frame1 = Frame(height="800", width="900")
        self.frame1.config(bg="#064663")
        self.frame1.pack(padx=30, pady=30)
        Button(self.frame1,text="Abrir Archivo", bg="#ECB365", fg="black", font=("Lemon Juice", 30), bd = 0, padx=5, command=self.abrir).place(x=600,y=100)
        Button(self.frame1,text="Analizar", bg="#0E8388", fg="#ffffff", font=("Lemon Juice",33), bd = 0, padx=28, command=self.analizar).place(x=600,y=200)
        Button(self.frame1,text="Errores", bg="#ECB365", fg="black", font = ("Lemon Juice",33), bd = 0, padx=28).place(x=600,y=300)
        Button(self.frame1,text="Salir", bg="#0E8388", fg="#ffffff", font=("Lemon Juice",33),anchor="center", bd=0,
                command= self.pantalla_principal.destroy,padx=52).place(x=600,y=400)
        self.mensaje = Text(self.frame1,width=30, height=15, font=("Lemon Juice", 22), bg="black", fg="light green", bd=0)
        self.mensaje.place(x=100, y=50)
        
        self.frame1.mainloop()
    
    def abrir(self):
        try:
            file = askopenfilename(title="Cargar un archivo", filetypes=[("Archivos", f'*.json')])
            self.text = file
            self.openfile = open(self.text, encoding="utf-8")
            self.archivo = self.openfile.read()
            self.mensaje.insert(INSERT, self.archivo)    
        except:
            print('Error, no se ha seleccionado ningún archivo')
        #print(self.archivo)

    def analizar(self):
        j = Analizador()
        j.Analisis(self.archivo)


p = Interfaz()