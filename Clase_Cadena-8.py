class Cadena():
    def __init__(self, cadena):
        self.cadena = cadena
        self.listaMinuscula = ['a','b']
        self.listaMayuscula = ['A','B']

    def find_encontrar(self,buscar):
        for i,v in enumerate(self.cadena):
            if v==buscar:
                return v
        return -1

Micadena=Cadena(None)
Micadena.find_encontrar('a')