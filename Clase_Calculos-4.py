class Calculos:
    def __init__(self,numero):
        self.numero=numero
    def paresEimpares(self):
        dicc = {'pares': [],'impares':[]}
        for num in range(self.numero):
            if num% 2 ==0:
                dicc['pares'].append(num)
            else:
                dicc['impares'].append(num)
        return dicc
Micalculo=Calculos(5)
Micalculo.paresEimpares()