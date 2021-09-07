class Vuelto:
    def __init__(self, costo,pago):
        self.__costo=costo
        self.__pago=pago
        self.billetes=[50,20,10,5,1]
    def obtenerVuelto(self):
        vuelto=self.__pago-self.__costo
        vueltos = []
        for moneda in self.__billetes:
            if vuelto>=moneda:
                billete=vuelto/moneda
                vuelto=vuelto%moneda
                vueltos.append({billete:moneda})
        return  vueltos

vue = Vuelto(53,100)
print(vue.obtenerVuelto())
