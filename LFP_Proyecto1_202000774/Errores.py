
class Error:
    def __init__(self):
        self.principal = '''
            {
        '''

    def lexemas(self, entrada, fila, columna, numero):
        error = '''
            {
                "No.1"
                "Descripción-Token":{
        '''
        
        error+=f'''
            "Numero":{numero}
            "Lexema":{entrada}
            "Tipo":Error
            "Columna":{columna}
            "Fila":{fila}
        '''
        error+="},"

        
        return error