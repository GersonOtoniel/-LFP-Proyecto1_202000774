import os

class Arboll:
    def __init__(self):
        self.graph = '''
            graph{
            
            
        '''

    def subarbol2(self, operacion, n1, n2, numsub, numnodo1, numnodo2, nodopr, resultado):   
    
        self.sub = f'''
            subgraph n{numsub}
        '''
        self.sub+='{'
        #self.graph+=self.sub
        
        nodop = f'''
            \n\t n{nodopr} [label="{operacion}  {resultado}"]
        '''
        self.sub+=nodop
        #nodop=''
        #--------------------------------------------------------------------
        nodos = f'''
            \n\t n{numnodo1} [label = "{n1}"]
        '''
        self.sub+=nodos

        relacion1 = f'''
            \n\t n{nodopr} -- n{numnodo1}
        '''
        self.sub+=relacion1
        #nodos=''
        #relacion1=''
        #----------------------------------------------------------------
        nodos2 = f'''
            \n\t n{numnodo2} [label = "{n2}"]
        '''
        self.sub+=nodos2
        relacion2 = f'''
            \n\t n{nodopr} -- n{numnodo2}
        '''
        self.sub+=relacion2
        self.sub+="}"
        #nodos2=''
        #relacion2=''
    
        return self.sub

    def subarbol1(self, operacion, n1 , numsub, nodopr, numnodo, resultado):
        self.sub = f'''
            subgraph n{numsub}
        '''
        self.sub+='{'
        #self.graph+=self.sub
        
        nodop = f'''
            \n\t n{nodopr} [label="{operacion}  {resultado}"]
        '''
        self.sub+=nodop
        #nodop=''
        #--------------------------------------------------------------------
        nodos = f'''
            \n\t n{numnodo} [label = "{n1}"]
        '''
        self.sub+=nodos

        relacion1 = f'''
            \n\t n{nodopr} -- n{numnodo}
        '''
        self.sub+=relacion1
        self.sub+="}"

        return self.sub
        
               

    def fin(self):
        self.graph+='}'
        with open("ejemplografica.dot", "w") as f:
            f.write(self.graph)

        os.system('dot -Tpdf ejemplografica.dot -o ejemplografica.pdf') 
