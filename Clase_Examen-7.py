class Examen:
    def __init__(self,lista=[]):
        self.lista=lista

    def ListaMenor(self,num):
        listaMenor=()
        for menor in self.lista:
            if menor>num:
                listaMenor.append(menor)
        return listaMenor

exa = Examen([2,5,20,16])
print(exa.ListaMenor(13))
respuesta = [2, 5]
