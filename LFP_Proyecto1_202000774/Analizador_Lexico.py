"""Analizador léxico"""
from Operaciones import Operaciones_Aritmeticas
from Operaciones import operaciones_trigonometricas
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
        self.creararbol()
        for i in self.lista_resultados:
            print(i)

           

    global j
    j = 0
    global nodoprincipa
    nodoprincipa = 100
    global nodo1
    nodo1 = 200
    global nodo2
    nodo2 = 300

    def arbol2(self):
        global j
        global nodoprincipa
        global nodo1
        global nodo2
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
                return '','','','','','','','',''  
            char = self.lista_de_lexemas[j]
            if self.lista_de_lexemas[j] == "Operacion":
                operacion = self.lista_de_lexemas[j+1]
                nodoprincipal = f''' n{nodoprincipa}[label="{operacion} '''
                nodoprincipa+=1
            if self.lista_de_lexemas[j] == "Valor1":
                if self.lista_de_lexemas[j+1] == "[":
                    j+=1
                    f = self.arbol2()
                    n1 = f[3]
                    n1_1 = f'''{f[0]}'''
                    extras0 = f''' {f[1]} \n {f[2]} \n {f[4]}\n {f[5]} \n{f[6]} \n {f[7]} '''
                else:
                    n1 = float(self.lista_de_lexemas[j+1])
                    n1_1 = f''' n{nodo1}[label = "{n1}"] '''
                    nodo1+=1
            if self.lista_de_lexemas[j] == "Valor2":
                if self.lista_de_lexemas[j+1] == "[":
                    j+=1
                    s = self.arbol2()
                    n2 = s[3]
                    n2_2 = f'''{s[0]}'''
                    extras = f''' {s[1]} \n {s[2]} \n {s[4]} \n {s[5]} \n{s[6]} \n {s[7]} '''
                else:
                    n2 = float(self.lista_de_lexemas[j+1])
                    n2_2=f''' n{nodo2}[label = "{n2}"] '''
                    nodo2+=1
            if operacion and n1 and n2 !='':
                if extras or extras =='' or extras0 or extras0=='':
                    j+=1
                    resultado = Operaciones_Aritmeticas.Operaciones_Aritmeticas(operacion,n1,n2).operar()
                    nodoprincipal+=f''' {resultado}"] '''
                    relacion = f''' n{nodoprincipal[2:5]}--n{n1_1[2:5]} '''
                    relacion2 = f''' n{nodoprincipal[2:5]}--n{n2_2[2:5]} '''
                    return nodoprincipal, relacion, relacion2, resultado, extras, extras0, n1_1, n2_2
            if operacion and n1 and n2 != '':
                operacion=''
                n1 = ''
                n2 = ''
            if n1 and operacion in ("Seno", "Coseno", "Tangente"):
                j+=1
                resultado2 = operaciones_trigonometricas.Operaciones_Trigonometricas(operacion, n1).operar()
                nodoprincipal+=f''' {resultado2}"] '''
                relacion3 = f''' n{nodoprincipal[2:5]}--n{n1_1[2:5]} '''
                relacion4 = f''''''
                return nodoprincipal, relacion3, relacion4, resultado2, extras, extras0, n1_1, n2_2
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
            nodopri = subarbol[0]
            rela1 = subarbol[1]
            rela2 = subarbol[2]
            nodoextra = subarbol[4]
            nodo1extra = subarbol[5]
            nod1 = subarbol[6]
            nod2 = subarbol[7]
            if subarbol:
                if nodopri and rela1 and rela2 and nod1 and nod2:
                    self.lista_de_arboles.append(nodopri)
                    subgraph+=nodopri
                    self.lista_de_arboles.append(rela1)
                    subgraph+=rela1
                    self.lista_de_arboles.append(rela2)
                    subgraph+=rela2
                    self.lista_de_arboles.append(nod1)
                    subgraph+=nod1
                    self.lista_de_arboles.append(nod2)
                    subgraph+=nod2
                if nodoextra:
                    self.lista_de_arboles.append(nodoextra)
                    subgraph+=nodoextra
                if nodo1extra:
                    self.lista_de_arboles.append(nodo1extra)
                    subgraph+=nodo1extra
                if nodopri =='' and rela1 == '' and rela2 == '' and nodo1extra == '' and nodoextra == '':
                    break
                subgraph+='}'
                self.graph+=subgraph
                n+=1
                subgraph = ''
                nodopri = ''
                rela1 = ''
                rela2 = ''
                nodoextra = ''
                nodo1extra = ''
      
        self.fin()


    def fin(self):
        self.graph+='}'
        with open("ejemplografica.dot", "w") as f:
            f.write(self.graph)

        os.system('dot -Tpng ejemplografica.dot -o ejemplografica.png') 

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

dificil = '''
{
{
    "Operacion":"Suma"
    "Valor1":4.5
    "Valor2":5.32 
},
{
    "Operacion":"Resta"
    "Valor1":[
        "Operacion":"Multiplicacion"
        "Valor1":505
        "Valor2":3
    ]
    "Valor2": [
        "Operacion":"Potencia"
        "Valor1":10
        "Valor2":[
            "Operacion":"Raiz"
            "Valor1":9
            "Valor2":[
                "Operacion":"Multiplicacion"
                "Valor1":2
                "Valor2":1
            ]
        ]
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
}
'''

#p = Analizador()
#p.Analisis(dificil)

