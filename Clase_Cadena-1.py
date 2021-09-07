class Cadena():
    def __init__(self, cadena):
        self.cadena = cadena
        self.Minuscula = ['a','b']
        self.Mayuscula = ['A','B']
    def mayMin(self):
        cmay,cmin=0,0
        for i,v in enumerate(self.cadena):
            if i in self.Mayuscula:
                cmay+=1
            elif i in self.Minuscula:
                cmin+=1
        return cmay, cmin
tarea=Cadena('Examen de POO')
print(tarea.mayMin())
respuesta = (4, 7)