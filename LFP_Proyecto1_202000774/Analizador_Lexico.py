"""Analizador léxico"""
from Operaciones import Operaciones_Aritmeticas
from Operaciones import operaciones_trigonometricas
from Arbol.Arbol import Arboll
import os


class Analizador:
    def __init__(self):
        self.fila = 1
        self.columna = 1
        self.Lista_de_lexemas1 = ["{", "}", "\"", "[", "]", ":", "-", ",",
                    ".", "Operacion", "Valor1", "Valor2", 
                    "Suma", "Resta", "Multiplicacion", "Division",
                    "Potencia", "Raiz", "Inverso", "Seno",
                    "Coseno", "Tangente", "Mod"]
        self.lista_de_lexemas = []
        self.lista_resultados = []
        self.lista_operaciones = []
        self.lista_de_arboles = []
        self.graph = '''
            graph{
            
            '''     

    def lista_lexemas(self):
        return self.lista_de_lexemas

    def Analisis(self, texto2):
        count1 = 0
        count2 = 0
        count3 = 0
        operaciones = ''
        lista_cada_operacion = []
        while texto2:
            char = texto2[count1]
            if char == "\n":
                self.fila+=1
                self.columna = 1
            if count1 == len(texto2)-1:
                break
            if char == "\"":
                count2+=1
                count1+=1
                self.columna+=1
                continue
            if char == "[" or char == "]":
                self.lista_de_lexemas.append(char)
            if char == "{" or char == "}":
                self.lista_de_lexemas.append(char)
            if count2 == 1:
                lexema = self.armar_lexemas(texto2[count1:])
                self.lista_de_lexemas.append(lexema)
                self.columna+=len(lexema)
                count1+=len(lexema)
                count2 = 0
            if char.isdigit() and texto2[count1+1]!="\"":
                numero = self.armar_numeros(texto2[count1:])
                self.lista_de_lexemas.append(numero)
                self.columna+=len(numero)
                count1+=len(numero)-1
            self.columna+=1
            count1+=1
        #self.revision()
        #for i in lista_de_lexemas:
        #   print(i)
        #print(lista_de_lexemas)
        self.añadir()
        #print("numero de filas: " + str(self.fila) + " numero de columnas: " + str(self.columna))
        #self.errores(self.lista_de_lexemas)


    def armar_lexemas(self, texto):
        lexema = ""
        for i in texto:
            if i == "\"":
                return lexema
            else:
                lexema+=i

    def armar_numeros(self, texto2):
        numero = ""
        for i in texto2:
            a = i
            if i.isdigit() or i==".":
                numero+=i
            if i in (" ", "\n", "\t", "\t"):
                return numero  

    def revision(self):
        corchetescierre = 0
        corchetesabre = 0
        count2 = 0
        operacion=''
        listacadaoperacion = []
        while count2<=len(self.lista_de_lexemas)-1:
            char = self.lista_de_lexemas[count2]
            if len(self.lista_de_lexemas)-1 == count2 and self.lista_de_lexemas[len(self.lista_de_lexemas)-1] and self.lista_de_lexemas[count2]== "}":
                break 
            if count2 == 0 and self.lista_de_lexemas[count2] == "{":
                count2+=1
                continue
            if self.lista_de_lexemas[count2] == "{":
                corchetesabre+=1
                count2+=1
                continue
            if self.lista_de_lexemas[count2] == "}":
                corchetescierre+=1
                count2+=1
            if corchetescierre==1:
                listacadaoperacion.append(operacion)
                corchetesabre = 0
                corchetescierre = 0 
                operacion=''
                continue
            if corchetesabre==1:
                operacion+=self.lista_de_lexemas[count2]
            count2+=1
        print(listacadaoperacion)


    global i
    i = 0
    def operar(self):
        global i
        operacion = ''
        n1 = ''
        n2 = ''
        while self.lista_de_lexemas:
            if i > len(self.lista_de_lexemas)-1:
                break
            char = self.lista_de_lexemas[i]
            if self.lista_de_lexemas[i] == "Operacion":
                operacion = self.lista_de_lexemas[i+1]
            if self.lista_de_lexemas[i] == "Valor1":
                if self.lista_de_lexemas[i+1] == "[":
                    i+=1
                    n1 = self.operar()
                else:
                    n1 = float(self.lista_de_lexemas[i+1])
            if self.lista_de_lexemas[i] == "Valor2":
                if self.lista_de_lexemas[i+1] == "[":
                    i+=1
                    n2 = self.operar()
                else:
                    n2 = float(self.lista_de_lexemas[i+1])
            if operacion and n1 and n2 != '':
                i+=1
                return Operaciones_Aritmeticas.Operaciones_Aritmeticas(operacion,n1,n2).operar()
            if operacion and n1 and n2 != '':
                operacion=''
                n1 = ''
                n2 = ''
            if n1 and operacion in ("Seno", "Coseno", "Tangente"):
                i+=1
                return operaciones_trigonometricas.Operaciones_Trigonometricas(operacion, n1).operar()
            if n1 and operacion in ("Seno", "Coseno", "Tangente"):
                operacion = ''
                n1 = ''
                n2 = ''
            else:
                i+=1
                continue
            
    def añadir(self):
        while True:
            operacion = self.operar()
            if operacion or operacion == float(0):
                self.lista_resultados.append(operacion)
            else:
                break
        #a = Arboll
        #self.subarbol(self.lista_de_lexemas)
        self.creararbol()
        for i in self.lista_resultados:
            print(i)

           

    global j
    j = 0
    def arbol2(self):
        global j
        s = ''
        f = ''
        operacion = ''
        n1 = ''
        n2 = ''
        n1_1=''
        n2_2=''
        extras = ''
        extras0 = ''
        while self.lista_de_lexemas:
            if j > len(self.lista_de_lexemas)-1:
                return '','','','','','',''
                
            char = self.lista_de_lexemas[j]
            if self.lista_de_lexemas[j] == "Operacion":
                operacion = self.lista_de_lexemas[j+1]
            if self.lista_de_lexemas[j] == "Valor1":
                if self.lista_de_lexemas[j+1] == "[":
                    j+=1
                    f = self.arbol2()
                    n1 = f[3]
                    n1_1 = f''' {f[0]} '''
                    extras0 = f''' {f[1]} \n {f[2]} '''
                else:
                    n1 = float(self.lista_de_lexemas[j+1])
                    n1_1 = f''' {n1} '''
            if self.lista_de_lexemas[j] == "Valor2":
                if self.lista_de_lexemas[j+1] == "[":
                    j+=1
                    s = self.arbol2()
                    n2 = s[3]
                    n2_2 = f''' {s[0]} '''
                    extras = f''' {s[1]} \n {s[2]} '''
                else:
                    n2 = float(self.lista_de_lexemas[j+1])
                    n2_2=f'''{n2}'''
            if operacion and n1 and n2 !='':
                if extras or extras =='':
                    j+=1
                    resultado = Operaciones_Aritmeticas.Operaciones_Aritmeticas(operacion,n1,n2).operar()
                    nodoprincipal = f''' "{operacion} {resultado}" '''
                    #v1 = f''' "{n1}" '''
                    #v2 = f''' "{n2}" '''
                    relacion = f''' {nodoprincipal} -- {n1_1} '''
                    relacion2 = f''' {nodoprincipal}--{n2_2} '''
                    return nodoprincipal, relacion, relacion2, resultado, extras, extras0
            if operacion and n1 and n2 != '':
                operacion=''
                n1 = ''
                n2 = ''
            if n1 and operacion in ("Seno", "Coseno", "Tangente"):
                j+=1
                resultado = operaciones_trigonometricas.Operaciones_Trigonometricas(operacion, n1).operar()
                nodoprincipal = f''' "{operacion}  {resultado}" '''
                relacion = f''' {nodoprincipal}--{n1_1} '''
                return nodoprincipal, relacion, resultado
            if n1 and operacion in ("Seno", "Coseno", "Tangente"):
                operacion = ''
                n1 = ''
                n2 = ''
            else:
                j+=1
                continue


    global n
    n = 0
    def creararbol(self):
        global n
       
        while True:
            subgraph = f''' subgraph s{n}  '''
            subgraph+='{'
            subarbol = self.arbol2()
            nodo1 = subarbol[0]
            nodo2 = subarbol[1]
            nodo3 = subarbol[2]
            nodoextra = subarbol[4]
            nodo1extra = subarbol[5]
            if subarbol:
                if nodo1:
                    self.lista_de_arboles.append(nodo1)
                    subgraph+=nodo1
                if nodo2:
                    self.lista_de_arboles.append(nodo2)
                    subgraph+=nodo2
                self.lista_de_arboles.append(nodo3)
                subgraph+=nodo3
                if nodoextra:
                    self.lista_de_arboles.append(nodoextra)
                    subgraph+=nodoextra
                if nodo1extra:
                    self.lista_de_arboles.append(nodo1extra)
                    subgraph+=nodo1extra
                if nodo1 =='' and nodo2 == '' and nodo3 == '' and nodo1extra == '' and nodoextra == '':
                    break
                subgraph+='}'
                self.graph+=subgraph
                n+=1
                subgraph = ''
                nodo1 = ''
                nodo2 = ''
                nodo3 = ''
                nodoextra = ''
                nodo1extra = ''
      
        self.fin()




    def fin(self):
        self.graph+='}'
        with open("ejemplografica.dot", "w") as f:
            f.write(self.graph)

        os.system('dot -Tpdf ejemplografica.dot -o ejemplografica.pdf') 

Entrada = '''
{
{
    "Operacion":"Suma"
    "Valor1":4.5
    "Valor2":5.3 
},
{
    "Operacion":"Resta"
    "Valor1":4.5
    "Valor2": [
        "Operacion":"Potencia"
        "Valor1":10
        "Valor2":3
    ]
},
{
    "Operacion":"Suma"
    "Valor1":5
    "Valor2":5.32
}
"Texto":"Realizacion de Operaciones"
"Color-Fondo-Nodo":"Amarillo"
"Color-Fuente-Nodo":"Rojo"
"Forma-Nodo":"Circulo"
}'''

Entrada2 = '''
{
{
    "Operacion":"Suma"
    "Valor1":4.5
    "Valor2":5.32 
},
{
    "Operacion":"Resta"
    "Valor1":4.6
    "Valor2": [
        "Operacion":"Potencia"
        "Valor1":10
        "Valor2":3
    ]
},
{
    "Operacion":"Suma"
    "Valor1":[
        "Operacion":"Potencia"
        "Valor1":9
        "Valor2":2
    ]
    "Valor2":5.3
}
"Texto":"Realizacion de Operaciones"
"Color-Fondo-Nodo":"Amarillo"
"Color-Fuente-Nodo":"Rojo"
"Forma-Nodo":"Circulo"
}'''



p = Analizador()
p.Analisis(Entrada2)

Entrada3 = '''
{
{
    "Operacion":"Suma"
    "Valor1":4.5
    "Valor2":5.32 
},
{
    "Operacion":"Resta"
    "Valor1":4.5
    "Valor2": [
        "Operacion":"Potencia"
        "Valor1":10
        "Valor2":3
    ]
},
{
    "Operacion":"Suma"
    "Valor1":[
        "Operacion":"Seno"
        "Valor1":90
    ]
    "Valor2":5.32
}
"Texto":"Realizacion de Operaciones"
"Color-Fondo-Nodo":"Amarillo"
"Color-Fuente-Nodo":"Rojo"
"Forma-Nodo":"Circulo"
}'''
