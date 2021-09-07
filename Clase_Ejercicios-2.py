class Ejercicios:
    def decimalBinario(self,decimal):
        binario=''
        while decimal // 2 != 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return decimal + binario

ejer = Ejercicios()
print(ejer.decimalBinario(5))
