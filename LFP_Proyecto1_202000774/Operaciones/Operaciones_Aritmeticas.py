

class Operaciones_Aritmeticas:
    def __init__(self, operacion, primero, segundo):
        self.operacion = operacion 
        self.primero = primero
        self.segundo = segundo
       
    def operar(self):
        if self.operacion == "Suma":
            return self.primero + self.segundo        
        if self.operacion == "Resta":
            return self.primero - self.segundo
        if self.operacion == "Multiplicacion":
            return self.primero * self.segundo
        if self.operacion == "Division":
            return self.primero/self.segundo
        if self.operacion == "Potencia":
            return self.primero ** self.segundo
        if self.operacion == "Raiz":
            return self.primero ** (1/self.segundo) 
        if self.operacion == "Inverso":
            return (1/self.primero)
        if self.operacion == "Modulo":
            return self.primero%self.segundo
        