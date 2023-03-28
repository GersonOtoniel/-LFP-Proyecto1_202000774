from fileinput import filename
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from tkinter import *
from tkinter import ttk
from Analizador_Lexico import Analizador
import webbrowser as wb

class Interfaz:
    def __init__(self):
        self.pantalla_principal = Tk()
        self.pantalla_principal.title("Pantalla Principal Proyecto 1")
        self.pantalla_principal.config(background="#04293A")
        #print(self.pantalla_principal.configure().keys())
        self.pantalla_principal.geometry("1300x600")
        self.pantalla_principal.resizable(0,0)
        self.frame()

    def frame(self):
        self.frame1 = Frame(height="900", width="1200")
        self.frame1.config(bg="#064663")
        self.frame1.pack(padx=30, pady=30)
        Button(self.frame1,text="Abrir Archivo", bg="#ECB365", fg="black", font=("Lemon Juice", 30), bd = 0, padx=5, command=self.abrir).place(x=1000,y=50)
        Button(self.frame1,text="Analizar", bg="#0E8388", fg="#ffffff", font=("Lemon Juice",33), bd = 0, padx=28, command=self.analizar).place(x=1000,y=170)
        Button(self.frame1,text="Errores", bg="#ECB365", fg="black", font = ("Lemon Juice",33), bd = 0, padx=28, command=self.Errore).place(x=1000,y=290)
        Button(self.frame1,text="Salir", bg="#0E8388", fg="#ffffff", font=("Lemon Juice",33),anchor="center", bd=0,
                command= self.pantalla_principal.destroy,padx=52).place(x=1000,y=410)
        self.mensaje = Text(self.frame1,width=50, height=14, font=("Arial", 20), fg="#ffffff", bd=0,bg='#315E73')
        self.mensaje.place(x=230, y=40)
        Button(self.frame1,text="Guardar", bg="#0E8388", fg="white", font = ("Lemon Juice",33), bd = 0, padx=28, command=self.guardad).place(x=30,y=50)
        Button(self.frame1,text="Guardar Como", bg="#ECB365", fg="black", font = ("Lemon Juice",33), bd = 0, padx=0).place(x=30,y=170)
        Button(self.frame1,text="Manual de Usuaro", bg="#0E8388", fg="white", font = ("Lemon Juice",28), bd = 0, padx=0, command=self.manualusuario).place(x=30,y=290)
        Button(self.frame1,text="Temas de Ayuda", bg="#ECB365", fg="black", font = ("Lemon Juice",30), bd = 0, padx=0, command=self.ayuda).place(x=30,y=410)
        
        self.frame1.mainloop()
    
    def abrir(self):
        try:
            self.file = askopenfilename(title="Cargar un archivo", filetypes=[("Archivos", f'*.json')])
            self.text = self.file
            self.openfile = open(self.text, encoding="utf-8")
            self.archivo = self.openfile.read()
            self.mensaje.delete(1.0,END)
            self.mensaje.insert(1.0, self.archivo)
            self.obtener()    
        except:
            print('Error, no se ha seleccionado ningún archivo')
        #print(self.archivo)

    def analizar(self):
        contenido = self.mensaje.get(1.0,END)
        j = Analizador()
        j.Analisis(self.leer)
        self.ventana_secundaria = Toplevel()
        self.ventana_secundaria.config(width=1000,height=100)
        self.mensaje.delete(1.0,END)

        photo = PhotoImage(file='./ejemplografica.png')
        txt =Text(self.ventana_secundaria, width=150, height=35,bg='black')
        txt.image_create(1.0, image=photo)
        txt.pack(anchor="center")
      
        self.ventana_secundaria.mainloop()
    def obtener(self):
        self.leer = self.mensaje.get(1.0,END)
        #print(self.leer)

    def guardarcomo(self):
        nuevo_Archivo = asksaveasfile(title='Guardar Archivo', defaultextension='.json', filetypes=(('Archivos de texto', '*.json'),))
        if nuevo_Archivo:
            contenido = self.mensaje.get(1.0,END)
            nuevo_Archivo.write(contenido)
            nuevo_Archivo.close()

    def guardad(self):
        if self.file != '':
            contenido = self.mensaje.get(1.0,END)
            fichero = open(self.file,'w+')
            fichero.write(contenido)
            fichero.close()
    
    def Errore(self):
        error = Analizador.errores
        self.mensaje.delete(1.0,END)
        self.mensaje.insert(1.0,error)

    def manualusuario(self):
        wb.open_new(r'D:\Desktop\SAN CARLOS\Lenguajes Formales y de Programación\Laboratorio\LFP_Proyecto1_202000774\Manual_de_Usuario.pdf')
            
    def ayuda(self):
        self.ventana_secundaria2 = Toplevel()
        self.ventana_secundaria2.config(width=150,height=150)
        nombre = Label(self.ventana_secundaria2, text="Gerson David Otoniel González Morales", font=22).pack()
        Auxiliar = Label(self.ventana_secundaria2, text="Auxiliar:  Diego Andrés Obin Rosales", font=22).pack()
        seccion = Label(self.ventana_secundaria2, text="Seccion: B+", font=22).pack()
        proyect = Label(self.ventana_secundaria2, text="Proyecto No. 1", font=22).pack()

p = Interfaz()