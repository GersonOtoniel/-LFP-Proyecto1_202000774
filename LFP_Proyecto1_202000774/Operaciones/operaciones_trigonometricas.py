from math import *

class Operaciones_Trigonometricas:
    def __init__(self, operacion, primero):
        self.operacion = operacion
        self.primero = primero

    def operar(self):
        if self.operacion == "Seno":
            return sin(self.primero)
        if self.primero == "Coseno":
            return cos(self.primero)
        if self.primero == "Tangente":
            return tan(self.primero)       
        