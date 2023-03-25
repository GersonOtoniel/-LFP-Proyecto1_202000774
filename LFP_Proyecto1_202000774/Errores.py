from Analizador_Lexico import Analizador

def errores(txt):
    count1=0
    while count1<=len(txt)-1:
        if txt[count1] in Analizador.lista_lexemas:
            print("Todo esta bien ")










Estructura_basica = '''
{
{
    "Operacion":"nombre"
    "Valor1":value
    "Valor2":value
}
}
'''

def estructura(entrada):
    lista = []
    for i in entrada:
        lista.append(i)
    print(lista)

Entrada = '''
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


estructura(Entrada)